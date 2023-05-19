import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from src.windows.tela_inicial import Ui_TelaInicial
from src.windows.tela_carregar_video import Ui_TelaCarregarVideo
from src.windows.tela_processamento import TelaProcessamento
from src.windows.tela_resultado import TelaResultado
from src.windows.select_image_area import WindowSelectArea
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtGui import QPixmap, QImage
import threading
import os
import cv2

from src.reduce_FPS_and_resolution import FormatVideo
 
class App():

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()

        # formato de video
        self.format_video = FormatVideo()

        # armazenar caminho do arquivo de video
        self.video_file_path = None

        # coordenas do retangulo
        self.coordinates = None

        # armazenar informações do arquivo de video
        self.video_info = None

        # carregar todas as telas
        self.tela_inicial = Ui_TelaInicial() # tela inicial
        self.tela_carregar_video = Ui_TelaCarregarVideo() # tela carregar video
        self.tela_processamento = TelaProcessamento() # tela processamento
        #self.tela_resultados = TelaResultados() # tela resultados

        self.init_main_window()
        self.MainWindow.show()

    # tela inicial
    def init_main_window(self):
       
        self.video_file_path = None
        self.video_info = None
       
        self.tela_inicial.setupUi(self.MainWindow) 
        self.tela_inicial.pushButton.clicked.connect(self.init_load_video_window)

    # tela carregar video
    def init_load_video_window(self):
        self.tela_inicial.video_player.stop()

        self.tela_carregar_video.setupUi(self.MainWindow)
        
        if self.video_file_path is not None:
            self.select_video_file()
        
        self.tela_carregar_video.pushButton_voltar.clicked.connect(self.init_main_window)
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

        if self.video_file_path is None:
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

            # iniciar tela de selecionar area
            self.tela_selecionar_area = WindowSelectArea(video_processed_path, self.MainWindow)
            
            self.tela_selecionar_area.show()
            self.tela_selecionar_area.button.clicked.connect(self.init_processing_window)
            
    def init_processing_window(self):
        self.tela_selecionar_area.close()
        self.tela_processamento.setupUi(self.MainWindow)


        self.tela_processamento.pushButton_cancelar.clicked.connect(self.cancel_processing)

    def cancel_processing(self):
        # finalizar processamento da yolov8n
        
        # voltar para de carregar video
        self.tela_processamento.pushButton_cancelar.clicked.connect(self.init_load_video_window)

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

        if self.video_file_path is None or self.video_file_path is '':
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())