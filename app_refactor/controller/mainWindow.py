from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow
from view.tela_inicial import Ui_TelaInicial
from view.tela_video_entrada import Ui_TelaVideoEntrada
from view.tela_stream import Ui_TelaStream, VideoProcessingThread
from view.tela_carregar_video import Ui_TelaCarregarVideo
from ultralytics import YOLO

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_inicial = Ui_TelaInicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_video_entrada = Ui_TelaVideoEntrada()
        self.tela_video_entrada.setupUi(self.stack1)

        self.tela_stream = Ui_TelaStream()
        self.tela_stream.setupUi(self.stack2)

        self.tela_carregar_video = Ui_TelaCarregarVideo()
        self.tela_carregar_video.setupUi(self.stack3)

        self.model = YOLO("yolov8n.pt")
        self.video_thread = None

        self.QtStack.addWidget(self.stack0) # tela inicial
        self.QtStack.addWidget(self.stack1) # tela video entrada
        self.QtStack.addWidget(self.stack2) # tela stream

        self.QtStack.addWidget(self.stack3) # tela carregar video


class Main(QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # botoes tela inicial
        self.tela_inicial.btn_realtime.clicked.connect(self.show_tela_video_entrada)
        self.tela_inicial.btn_video.clicked.connect(self.show_tela_carregar_video)

        # botoes tela carregar video
        self.tela_carregar_video.pushButton_voltar.clicked.connect(self.show_tela_inicial)
        #self.tela_carregar_video.pushButton_rastrear.clicked.connect(self.show_tela_processando)
        
        # botoes tela video entrada
        self.tela_video_entrada.back_button.clicked.connect(self.show_tela_inicial)
        self.tela_video_entrada.track_button.clicked.connect(self.show_tela_rastrear)

        

        # botoes tela stream
        self.tela_stream.btn_voltar.clicked.connect(self.show_tela_video_entrada)

    def show_tela_inicial(self):
        self.QtStack.setCurrentIndex(0)

    def show_tela_carregar_video(self):
        self.QtStack.setCurrentIndex(3)

    def show_tela_video_entrada(self):
        # perguntar se a thread de stream está rodando
        if self.video_thread:
            if self.video_thread.running[0]:
                self.video_thread.running[0] = False
        
        self.QtStack.setCurrentIndex(1)

    def show_tela_rastrear(self):
        # capturar as informações na tela
        if self.tela_video_entrada.radioButton_intelbras.isChecked():
            # intelbras
            user = self.tela_video_entrada.user_input.text()
            user_pass = self.tela_video_entrada.pass_input.text() 
            camera_channel = self.tela_video_entrada.channel_input.text() 

            # iniciar thread de realtime
            self.video_thread = VideoProcessingThread(model=self.model, target_fps=5, new_width=640, main_window=self.tela_stream)
            self.video_thread.video_path = f"rtsp://{user}:{user_pass}@192.168.0.102:554/cam/realmonitor?channel={camera_channel}&subtype=0"
            self.video_thread.running[0] = True
            self.video_thread.start_processing()
        
        else:
            # webcam
            camera = 0

            # iniciar thread de realtime
            self.video_thread = VideoProcessingThread(model=self.model, target_fps=5, new_width=640, main_window=self.tela_stream)
            self.video_thread.video_path = 0
            self.video_thread.running[0] = True
            self.video_thread.start_processing()

            
        self.QtStack.setCurrentIndex(2)

