import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from view.video_processing.tela_carregar_video import Ui_TelaCarregarVideo
from view.video_processing.tela_processamento import TelaProcessamento
from view.video_processing.tela_resultado import TelaResultado
from view.video_processing.select_image_area import WindowSelectArea
from PyQt5.QtWidgets import QFileDialog, QStyle 
from PyQt5.QtGui import QPixmap, QImage, QDesktopServices
from src.detect_and_track import *
import os
import cv2

from src.reduce_FPS_and_resolution import FormatVideo

def detect_display_server():
    # Verifica se a variável de ambiente XDG_SESSION_TYPE está definida
    if 'XDG_SESSION_TYPE' in os.environ:
        # Obtém o valor da variável de ambiente XDG_SESSION_TYPE
        session_type = os.environ['XDG_SESSION_TYPE']
        # Verifica se o servidor de exibição é Wayland
        if session_type == 'wayland':
            return 'wayland'
    # Se não detectar Wayland, assume-se que está usando Xorg
    return 'xorg'

def configure_qt_platform():
    display_server = detect_display_server()
    if display_server == 'wayland':
        # Define a variável de ambiente QT_QPA_PLATFORM como wayland
        os.environ['QT_QPA_PLATFORM'] = 'wayland'
    else:
        # Define a variável de ambiente QT_QPA_PLATFORM como xcb para usar Xorg
        os.environ['QT_QPA_PLATFORM'] = 'xcb'

# Chama a função para configurar a plataforma Qt de acordo com o servidor de exibição
configure_qt_platform()

class App():

    def __init__(self, MainWindow, QtStack):
        self.MainWindow = MainWindow
        self.QtStack = QtStack

        # Resultados do processamento do vídeo
        self.results = None

        # para guardar os layouts dinamicos da tela de resultados
        self.dynamic_layouts = []

        # posição do slider na tela de resultados
        self.slider_position = 1

        # formato de video
        self.format_video = FormatVideo()

        # armazenar caminho do arquivo de video
        self.video_file_path = None

        # coordenadas do retangulo
        self.coordinates = None

        # armazenar informações do arquivo de video
        self.video_info = None

        # estado do processamento do video
        self.processing_status = False

        # carregar todas as telas
        self.tela_carregar_video = Ui_TelaCarregarVideo() # tela carregar video
        self.tela_processamento = TelaProcessamento() # tela processamento
        self.tela_resultados = TelaResultado() # tela resultados

        self.init_load_video_window()

    def show_tela_inicial(self):

        self.video_file_path = None
        self.tela_carregar_video.label_rsp_nome_do_arquivo.setText("")
        self.tela_carregar_video.label_rsp_dimensao.setText("")
        self.tela_carregar_video.label_rsp_tamanho.setText("")
        self.tela_carregar_video.label_nome_arquivo.setText("")
        self.tela_carregar_video.label_7.setPixmap(QtGui.QPixmap())

        self.tela_carregar_video.label_7.setMinimumSize(QtCore.QSize(400, 230))
        self.tela_carregar_video.label_7.setMaximumSize(QtCore.QSize(400, 230))
        self.tela_carregar_video.label_7.setObjectName("label_7")
        self.tela_carregar_video.label_7.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.QtStack.setCurrentIndex(0)
    
    # tela carregar video
    def init_load_video_window(self):

        self.tela_carregar_video.setupUi(self.MainWindow)
        
        if self.video_file_path is not None:
            self.select_video_file()
        
        self.tela_carregar_video.pushButton_voltar.clicked.connect(self.show_tela_inicial)
        self.tela_carregar_video.pushButton_carregar_video.clicked.connect(self.select_video_file)
        
        self.tela_carregar_video.checkBox_reduzir_dimensao.stateChanged.connect(self.show_lineedit_dimensao)
        self.tela_carregar_video.checkBox_reduzir_fps.stateChanged.connect(self.show_lineedit_fps)

        self.tela_carregar_video.lineEdit_dimensao_1.textChanged.connect(self.validate_dimensao_1)
        self.tela_carregar_video.lineEdit_dimensao_2.textChanged.connect(self.validate_dimensao_2)
        self.tela_carregar_video.lineEdit_fps.textChanged.connect(self.validate_fps)

        self.tela_carregar_video.pushButton_rastrear.clicked.connect(self.verify_and_init_processing)

    # verifica se é possivel iniciar o processamento e inicia a tela de selecionar area
    def verify_and_init_processing(self):

        width = None
        height = None 
        fps = None

        if self.video_file_path == '' or self.video_file_path is None:
            self.tela_carregar_video.label_erro_video_nao_selecionado.setVisible(True)
        else:
            # video foi carregado
            # se o checkbox de reduzir dimensao estiver marcado, verificar se os campos de dimensao estao preenchidos corretamente
            if self.tela_carregar_video.checkBox_reduzir_dimensao.isChecked():
                if self.tela_carregar_video.lineEdit_dimensao_1.text() == "" or self.tela_carregar_video.lineEdit_dimensao_2.text() == "":
                    self.tela_carregar_video.label_erro_dimensao.setText("Preencha as dimensões")
                    self.tela_carregar_video.label_erro_dimensao.setVisible(True)
                    return
                else:
                    # verificar se ambas as dimensoes são menores que a do video
                    if int(self.tela_carregar_video.lineEdit_dimensao_1.text()) > self.video_info['width'] or int(self.tela_carregar_video.lineEdit_dimensao_2.text()) > self.video_info['height']:
                        self.tela_carregar_video.label_erro_dimensao.setText("Dimensões maiores que o video")
                        self.tela_carregar_video.label_erro_dimensao.setVisible(True)
                        return
                    else:
                        width = int(self.tela_carregar_video.lineEdit_dimensao_1.text())
                        height = int(self.tela_carregar_video.lineEdit_dimensao_2.text())
            
            # se o checkbox de reduzir fps estiver marcado, verificar se o campo de fps esta preenchido corretamente
            if self.tela_carregar_video.checkBox_reduzir_fps.isChecked():
                if self.tela_carregar_video.lineEdit_fps.text() == "":
                    self.tela_carregar_video.label_erro_fps.setText("Preencha o fps")
                    self.tela_carregar_video.label_erro_fps.setVisible(True)
                    return
                else:
                    # verificar se o fps é menor que o fps do video
                    if int(self.tela_carregar_video.lineEdit_fps.text()) > self.video_info['fps']:
                        self.tela_carregar_video.label_erro_fps.setText("Fps maior que o video")
                        self.tela_carregar_video.label_erro_fps.setVisible(True)
                        return
                    else:
                        fps = int(self.tela_carregar_video.lineEdit_fps.text())
            # tudo certo, iniciar processamento do vídeo
            # capturar os valores
            
            # processado o video
            video_processed_path = self.format_video.reduce_resolution_and_fps(self.video_file_path, (width, height), fps)
            self.video_file_path = video_processed_path

            # iniciar tela de selecionar area
            self.tela_selecionar_area = WindowSelectArea(video_processed_path, self.MainWindow)
            
            self.tela_selecionar_area.show()
            self.tela_selecionar_area.button.clicked.connect(self.init_processing_window)
            
    # iniciar processamento do vídeo
    def init_processing_window(self):

        self.coordinates = self.tela_selecionar_area.coordinates

        if not self.coordinates:
            self.coordinates = {
                'x':{
                    'min': 0,
                    'max': self.video_info['width']
                }
                ,
                'y':{
                    'min': 0,
                    'max': self.video_info['height']
                }
            }

        self.tela_selecionar_area.close()
        self.tela_processamento.setupUi(self.MainWindow)
        
        self.detect_and_track_thread = DetectAndTrackThread('yolov8n', self.video_file_path, self.tela_processamento, self.coordinates, frame_a_frame=True)
        self.detect_and_track_thread.finished.connect(self.present_results)
        self.detect_and_track_thread.start()

        self.tela_processamento.pushButton_cancelar.clicked.connect(self.cancel_processing)

    def insert_results_on_layout(self):

        if self.tela_resultados.checkBox.isChecked():
            self.clear_dynamic_widgets()

            # inserir dados do frame a frame

             # adicionar a quantidade total de pessoas detectadas
            _translate = QtCore.QCoreApplication.translate
            self.tela_resultados.label_3.setText(_translate("MainWindow", f"{len(list(self.results[self.slider_position]['id']))} Pessoas detectadas"))

            # Numero da pessoa
            # velocidade
            # Tempo em video
            # people_number, velocity, time_in_video

            # criando um componenta para detecção  
            for id in list(self.results[self.slider_position]['id']):
                velocity = self.results[self.slider_position]['velocity'][id]
                time_in_video = self.results[self.slider_position]['detection_time'][id]

                self.create_component(self.tela_resultados, id, velocity, time_in_video)

            # criando vertical spacer
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.tela_resultados.verticalLayout_3.addItem(spacerItem)

        else:
            self.clear_dynamic_widgets()

            # adicionar a quantidade total de pessoas detectadas
            _translate = QtCore.QCoreApplication.translate
            self.tela_resultados.label_3.setText(_translate("MainWindow", f"{len(list(self.results['full_video']['id']))} Pessoas detectadas"))

            # Numero da pessoa
            # velocidade
            # Tempo em video
            # people_number, velocity, time_in_video

            # criando um componenta para detecção  
            for id in list(self.results['full_video']['id']):
                velocity = self.results['full_video']['velocity'][id]
                time_in_video = self.results['full_video']['detection_time'][id]

                self.create_component(self.tela_resultados, id, velocity, time_in_video)

            # criando vertical spacer
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.tela_resultados.verticalLayout_3.addItem(spacerItem)

    def clear_dynamic_widgets(self):
        for layout in self.dynamic_layouts:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                elif item.layout() is not None:
                    self.clear_dynamic_widgets_from_layout(item.layout())

        # Esvazia a lista depois de limpar os layouts
        self.dynamic_layouts = []

    def present_results(self):
        # apresentar os resultados na tela de resultados
        self.tela_resultados.setupUi(self.MainWindow)
        self.tela_resultados.pushButton_voltar.clicked.connect(self.init_load_video_window)

        self.tela_resultados.pushButton_open_folder.clicked.connect(self.open_result_folder)

        self.results = self.detect_and_track_thread.get_results()

        self.tela_resultados.pushButton_play_pause.setIcon(self.MainWindow.style().standardIcon(QStyle.SP_MediaPlay))

        # determinando a midia
        file_name = self.results["output_video_directory"]
        self.tela_resultados.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))

        self.tela_resultados.pushButton_play_pause.clicked.connect(self.play_pause)

        self.tela_resultados.horizontalSlider.sliderMoved.connect(self.set_position)
        self.tela_resultados.horizontalSlider.sliderReleased.connect(self.update_results)

        # MEDIA PLAYER
        #self.tela_resultados.media_player.stateChanged.connect(self.update_buttons)
        self.tela_resultados.media_player.positionChanged.connect(self.update_slider)
        self.tela_resultados.media_player.durationChanged.connect(self.update_duration)

        self.tela_resultados.checkBox.stateChanged.connect(self.insert_results_on_layout)

        # Limpar o layout antes de adicionar novos componentes
        self.clear_dynamic_widgets()

        # verificar se a função detect_and_track está ativado
        # afunção de analise frame a frame só aparece na tela do usuário se ele tiver inserido ela na tela anterior
    
        # adicionar a quantidade total de pessoas detectadas
        _translate = QtCore.QCoreApplication.translate
        self.tela_resultados.label_3.setText(_translate("MainWindow", f"{len(list(self.results['full_video']['id']))} Pessoas detectadas"))

        # Numero da pessoa
        # velocidade
        # Tempo em video
        # people_number, velocity, time_in_video

        # criando um componenta para detecção  
        for id in list(self.results['full_video']['id']):
            velocity = self.results['full_video']['velocity'][id]
            time_in_video = self.results['full_video']['detection_time'][id]

            self.create_component(self.tela_resultados, id, velocity, time_in_video)

        # criando vertical spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tela_resultados.verticalLayout_3.addItem(spacerItem)

    def open_result_folder(self):
        # Caminho da pasta que deseja abrir
        result_folder_path = os.path.join(os.getcwd(), "resultados")  # Altere para o caminho desejado
        QDesktopServices.openUrl(QUrl.fromLocalFile(result_folder_path))

    def play_pause(self):
        if self.tela_resultados.media_player.state() == QMediaPlayer.PlayingState:
            self.tela_resultados.media_player.pause()
  
            position_ms = self.tela_resultados.media_player.position()

            # Calcula o número do frame
            self.slider_position = int(position_ms * self.video_info['fps'] / 1000)


            self.insert_results_on_layout()
            self.tela_resultados.pushButton_play_pause.setIcon(self.MainWindow.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.tela_resultados.media_player.play()
            self.tela_resultados.pushButton_play_pause.setIcon(self.MainWindow.style().standardIcon(QStyle.SP_MediaPause))
            
    def update_results(self):
        # atualizar as informacoes do video apenas se a funcao frame a frame estiver ativada
        if self.tela_resultados.checkBox.isChecked():
            self.insert_results_on_layout()

    def set_position(self, position):
        self.tela_resultados.media_player.setPosition(position)
        self.slider_position = int(((position / 9000) * (self.results['total_frames'] - 1)) + 1)
 
    def update_slider(self, position):
        self.tela_resultados.horizontalSlider.setValue(position)
    
    def update_duration(self, duration):
        self.tela_resultados.horizontalSlider.setRange(0, duration)
        #self.label_duration.setText(f"Duration: {duration_in_seconds:.2f} seconds")
    
    def cancel_processing(self):
        self.detect_and_track_thread.terminate()
        self.detect_and_track_thread.wait()

        self.init_load_video_window()

    def validate_dimensao_1(self):
        # validar se o valor é menor que a dimensao do video e maior que 0
        text = self.tela_carregar_video.lineEdit_dimensao_1.text()
        if text != "":
            try:
                if int(text) > self.video_info['width'] or int(text) <= 0:
                    self.tela_carregar_video.label_erro_dimensao.setText("A largura deve ser menor que " + str(self.video_info['width']))
                    self.tela_carregar_video.label_erro_dimensao.setVisible(True)
                else:
                    self.tela_carregar_video.label_erro_dimensao.setVisible(False)
            except TypeError:
                self.tela_carregar_video.label_erro_dimensao.setText("Vídeo não carregado")
                self.tela_carregar_video.label_erro_dimensao.setVisible(True)
        else:
            self.tela_carregar_video.label_erro_dimensao.setVisible(False)
    
    def validate_dimensao_2(self):
        # validar se o valor é menor que a dimensao do video e maior que 0
        text = self.tela_carregar_video.lineEdit_dimensao_2.text()
        if text != "":
            try:
                if int(text) > self.video_info['height'] or int(text) <= 0:
                    self.tela_carregar_video.label_erro_dimensao.setText("A altura deve ser menor que " + str(self.video_info['height']))
                    self.tela_carregar_video.label_erro_dimensao.setVisible(True)
                else:
                    self.tela_carregar_video.label_erro_dimensao.setVisible(False)
            except TypeError:
                self.tela_carregar_video.label_erro_dimensao.setText("Vídeo não carregado")
                self.tela_carregar_video.label_erro_dimensao.setVisible(True)
        else:
            self.tela_carregar_video.label_erro_dimensao.setVisible(False)

    def validate_fps(self):
        # validar se o valor é menor que o fps do video e maior que 0
        text = self.tela_carregar_video.lineEdit_fps.text()
        if text != "":
            try:
                if int(text) > self.video_info['fps'] or int(text) <= 0:
                    self.tela_carregar_video.label_erro_fps.setText("Fps maior que o video")
                    self.tela_carregar_video.label_erro_fps.setVisible(True)
                else:
                    self.tela_carregar_video.label_erro_fps.setVisible(False)
            except TypeError:
                self.tela_carregar_video.label_erro_fps.setText("Vídeo não carregado")
                self.tela_carregar_video.label_erro_fps.setVisible(True)

    def show_lineedit_dimensao(self, state):
        # Define a visibilidade do QLineEdit baseado no estado do QCheckBox
        if state == Qt.Checked:
            self.tela_carregar_video.lineEdit_dimensao_1.setVisible(True)
            self.tela_carregar_video.lineEdit_dimensao_2.setVisible(True)
            self.tela_carregar_video.label_x.setVisible(True)
        else:
            self.tela_carregar_video.lineEdit_dimensao_1.setVisible(False)
            self.tela_carregar_video.lineEdit_dimensao_2.setVisible(False)
            self.tela_carregar_video.label_x.setVisible(False)
            self.tela_carregar_video.label_erro_dimensao.setVisible(False)

    def show_lineedit_fps(self, state):
        # Define a visibilidade do QLineEdit baseado no estado do QCheckBox
        if state == Qt.Checked:
            self.tela_carregar_video.lineEdit_fps.setVisible(True)
            self.tela_carregar_video.label_fps.setVisible(True)
        else:
            self.tela_carregar_video.lineEdit_fps.setVisible(False)
            self.tela_carregar_video.label_fps.setVisible(False)
            self.tela_carregar_video.label_erro_fps.setVisible(False)

    def select_video_file(self):    

        if self.video_file_path is None or self.video_file_path == '':
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.video_file_path, _ = QFileDialog.getOpenFileName(None, "Selecione o arquivo de vídeo", "", "Arquivos de Vídeo (*.mp4 *.avi *.mkv *.mov)", options=options)

        if self.video_file_path:
            # escrever no label o nove do arquivo
            self.tela_carregar_video.label_nome_arquivo.setText(self.video_file_path.split("/")[-1])

            # capturar informações do arquivo de video
            self.get_video_info()

            # escrever informações do arquivo de video
            self.tela_carregar_video.label_rsp_nome_do_arquivo.setText(self.video_file_path.split("/")[-1])
            self.tela_carregar_video.label_rsp_dimensao.setText(f"{self.video_info['width']}x{self.video_info['height']} pixels")
            self.tela_carregar_video.label_rsp_tamanho.setText(f"{self.video_info['size']:.2f} {self.video_info['size_unit']}")

            self.tela_carregar_video.label_erro_video_nao_selecionado.setVisible(False)

            # Carrega o vídeo usando a biblioteca OpenCV
            cap = cv2.VideoCapture(self.video_file_path)
            ret, frame = cap.read()

            # Extrai o primeiro frame e converte para o formato de imagem do PyQt
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pixmap = self.resize_frame(frame)

                w = pixmap.width()
                h = pixmap.height()

                self.tela_carregar_video.label_7.setMinimumSize(QtCore.QSize(w, h))
                self.tela_carregar_video.label_7.setMaximumSize(QtCore.QSize(w, h))
                self.tela_carregar_video.label_7.setPixmap(pixmap)
                self.tela_carregar_video.label_7.setStyleSheet("padding-left: 0px;")

    # pode ser em outro arquivo
    def get_video_info(self):
        # Verifica se o arquivo existe
        if not os.path.isfile(self.video_file_path):
            raise ValueError("O arquivo de vídeo não existe.")
        
        # Abre o arquivo de vídeo
        cap = cv2.VideoCapture(self.video_file_path)
        
        # Extrai as informações de dimensão
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Extrai as informações de tamanho
        file_size = os.path.getsize(self.video_file_path)
        size_unit = 'B'
        if file_size >= 1024*1024:
            file_size = file_size / (1024*1024)
            size_unit = 'MB'
        elif file_size >= 1024:
            file_size = file_size / 1024
            size_unit = 'KB'
        
        # Fecha o arquivo de vídeo
        cap.release()
        
        self.video_info = {'width': width, 'height': height, 'fps': fps, 'size': file_size, 'size_unit': size_unit}

    # pode ser em outro arquivo
    def resize_frame(self, frame, max_width=400, max_height=230):
        # Obtém as dimensões do frame de imagem
        height, width = frame.shape[:2]

        # Calcula a proporção da imagem
        ratio = min(max_width / width, max_height / height)

        # Calcula as novas dimensões da imagem com base na proporção
        new_width = int(width * ratio)
        new_height = int(height * ratio)

        # Redimensiona a imagem usando a função cv2.resize
        resized = cv2.resize(frame, (new_width, new_height))

        # Converte o frame redimensionado em um QPixmap
        qimage = QImage(resized.data, new_width, new_height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)

        return pixmap
    
    def create_component(self, window, people_number, velocity, time_in_video):
        # criar o vertical layout
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")

        # criar o titulo da pessoa
        label_titulo_pessoa = QtWidgets.QLabel(window.scrollAreaWidgetContents)
        label_titulo_pessoa.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        label_titulo_pessoa.setFont(font)
        label_titulo_pessoa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(28, 38, 38);\n"
                                          "padding: 8px;\n"
                                          "border-radius: 10px;")
        label_titulo_pessoa.setObjectName("label_titulo_pessoa")
        verticalLayout.addWidget(label_titulo_pessoa)

        # informações
        frame = QtWidgets.QFrame(window.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
        frame.setSizePolicy(sizePolicy)
        frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame")
        formLayout = QtWidgets.QFormLayout(frame)
        formLayout.setContentsMargins(-1, -1, 20, -1)
        formLayout.setObjectName("formLayout")
        label_rsp_tempo = QtWidgets.QLabel(frame)
        label_rsp_tempo.setStyleSheet("color: rgb(255, 255, 255);")
        label_rsp_tempo.setObjectName("label_rsp_tempo")
        formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, label_rsp_tempo)
        label_velocidade = QtWidgets.QLabel(frame)
        label_velocidade.setStyleSheet("color: rgb(255, 255, 255);")
        label_velocidade.setObjectName("label_velocidade")
        formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, label_velocidade)
        label_rsp_velocidade = QtWidgets.QLabel(frame)
        label_rsp_velocidade.setStyleSheet("color: rgb(255, 255, 255);")
        label_rsp_velocidade.setObjectName("label_rsp_velocidade")
        formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, label_rsp_velocidade)
        label_tempo = QtWidgets.QLabel(frame)
        label_tempo.setLayoutDirection(QtCore.Qt.LeftToRight)
        label_tempo.setStyleSheet("color: rgb(255, 255, 255);")
        label_tempo.setObjectName("label_tempo")
        formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, label_tempo)
        verticalLayout.addWidget(frame)

        # Adicionar o layout dinâmico à lista para remoção posterior
        self.dynamic_layouts.append(verticalLayout)
        
        window.verticalLayout_3.addLayout(verticalLayout)

        # Definir valores dos textos
        _translate = QtCore.QCoreApplication.translate
        label_titulo_pessoa.setText(_translate("MainWindow", f"Pessoa {people_number}"))

        formatted_time = time_in_video.strftime("%H:%M:%S.%f")[:-3]
        label_rsp_tempo.setText(_translate("MainWindow", f"{formatted_time}"))
        label_velocidade.setText(_translate("MainWindow", "Velocidade: "))
        label_rsp_velocidade.setText(_translate("MainWindow", f"{velocity:.2f} pixels/frame"))
        label_tempo.setText(_translate("MainWindow", "Tempo no vídeo:"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())