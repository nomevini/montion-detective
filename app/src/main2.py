import sys
from PyQt5 import QtWidgets
from windows.tela_inicial import Ui_TelaInicial
from windows.tela_carregar_video import Ui_TelaCarregarVideo
from windows.tela_processamento import TelaProcessamento
from windows.tela_resultado import TelaResultado
 
class App():

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()

        # carregar todas as telas
        self.tela_inicial = Ui_TelaInicial() # tela inicial
        self.tela_carregar_video = Ui_TelaCarregarVideo() # tela carregar video
        self.tela_processamento = TelaProcessamento() # tela processamento
        #self.tela_resultados = TelaResultados() # tela resultados

        self.init_main_window()
        self.MainWindow.show()

    # tela inicial
    def init_main_window(self):
       self.tela_inicial.setupUi(self.MainWindow) 
       self.tela_inicial.pushButton.clicked.connect(self.init_load_video_window)

    # tela carregar video
    def init_load_video_window(self):
        self.tela_carregar_video.setupUi(self.MainWindow)
        self.tela_carregar_video.pushButton_voltar.clicked.connect(self.init_main_window)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())