import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from model.realtime import *

class VideoProcessingThread(QObject):
    finished = pyqtSignal()

    def __init__(self, parent=None, model=None, video_path=None, new_width=None, target_fps=None, main_window=None, alert=[False]):
        super().__init__(parent)
        self.model = model
        self.video_path = video_path
        self.new_width = new_width
        self.target_fps = target_fps
        self.main_window = main_window
        self.running = [False]
        self.alert = alert

    def process_video(self):
        process_video(self.video_path, self.model, self.new_width, self.target_fps, self.main_window, thread_running=self.running, alert=self.alert)
        self.finished.emit()  # Emite o sinal quando a segunda thread terminar

    def start_processing(self):
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.process_video)
        self.finished.connect(self.thread.quit)
        self.finished.connect(self.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


class Ui_TelaStream(object):
    def setupUi(self, TelaStream):
        TelaStream.setObjectName("TelaStream")
        TelaStream.resize(1119, 698)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaStream.sizePolicy().hasHeightForWidth())
        TelaStream.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        TelaStream.setFont(font)
        TelaStream.setAutoFillBackground(False)
        TelaStream.setStyleSheet("background-color: rgb(33, 46, 46);")
        self.centralwidget = QtWidgets.QWidget(TelaStream)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame_2.setStyleSheet("border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pessoas_detectadas = QtWidgets.QLabel(self.frame_2)
        self.label_pessoas_detectadas.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_pessoas_detectadas.setFont(font)
        self.label_pessoas_detectadas.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-top: 10px;")
        self.label_pessoas_detectadas.setObjectName("label_pessoas_detectadas")
        self.verticalLayout.addWidget(self.label_pessoas_detectadas, 0, QtCore.Qt.AlignHCenter)

        # Substitua o widget de vídeo por um QLabel para mostrar imagens
        self.image_label = QtWidgets.QLabel(self.frame_2)
        self.image_label.setMinimumSize(QtCore.QSize(640, 360))
        self.image_label.setMaximumSize(QtCore.QSize(400, 230))
        self.image_label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 406, 582))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 90, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.frame1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame1.setObjectName("frame1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_6.setContentsMargins(1, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton {\n"
"    /* Estilo básico do QRadioButton */\n"
"    spacing: 10px; /* Espaço entre o botão e o texto */\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    font-size: 18px; /* Tamanho da fonte */\n"
"    padding: 5px; /* Espaçamento interno */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    /* Estilo do indicador (botão circular) */\n"
"    width: 15px; /* Largura do círculo */\n"
"    height: 15px; /* Altura do círculo */\n"
"    border-radius: 7px; /* Para garantir um formato circular */\n"
"    border: 2px solid rgb(255, 255, 255); /* Cor da borda do círculo */\n"
"    background-color: rgb(68, 88, 88); /* Cor de fundo do círculo */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    /* Estilo do indicador quando o mouse está sobre ele */\n"
"    border: 2px solid rgb(85, 170, 255); /* Cor da borda ao passar o mouse */\n"
"    background-color: rgb(50, 70, 70); /* Cor de fundo ao passar o mouse */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    /* Estilo do indicador quando está selecionado */\n"
"    background-color: rgb(85, 170, 255); /* Cor de fundo quando selecionado */\n"
"    border: 2px solid rgb(85, 170, 255); /* Cor da borda quando selecionado */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    /* Estilo do indicador selecionado quando o mouse está sobre ele */\n"
"    background-color: rgb(70, 150, 235); /* Cor de fundo ao passar o mouse */\n"
"    border: 2px solid rgb(70, 150, 235); /* Cor da borda ao passar o mouse */\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"    /* Estilo quando o QRadioButton está desabilitado */\n"
"    color: rgb(150, 150, 150); /* Cor do texto quando desabilitado */\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    /* Estilo do indicador quando o QRadioButton está desabilitado */\n"
"    background-color: rgb(80, 80, 80); /* Cor de fundo quando desabilitado */\n"
"    border: 2px solid rgb(120, 120, 120); /* Cor da borda quando desabilitado */\n"
"}\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)

        self.verticalLayout_3.addWidget(self.frame1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setMinimumSize(QtCore.QSize(60, 0))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_voltar = QtWidgets.QPushButton(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_voltar.sizePolicy().hasHeightForWidth())
        self.btn_voltar.setSizePolicy(sizePolicy)
        self.btn_voltar.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setStyleSheet("QPushButton{\n"
"    background: rgb(68, 88, 88);\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(47, 61, 61);\n"
"}\n"
"\n"
"\n"
"QToolTip{\n"
"    padding: 2px;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_voltar.setObjectName("btn_voltar")
        self.verticalLayout_7.addWidget(self.btn_voltar, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.verticalFrame)
        TelaStream.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaStream)
        QtCore.QMetaObject.connectSlotsByName(TelaStream)

    def update_image(self, frame, people_counter):
        # Converta o frame para o formato RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = frame_rgb.shape
        bytes_per_line = 3 * width

        q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Redimensione o pixmap para o tamanho disponível em proporção com o image_label
        pixmap = QPixmap.fromImage(q_image).scaledToWidth(self.image_label.width(), Qt.SmoothTransformation)

        # Defina o pixmap ajustado como a imagem exibida no image_label
        self.image_label.setPixmap(pixmap)

        _translate = QtCore.QCoreApplication.translate
        if people_counter == 1:
            self.label_pessoas_detectadas.setText(_translate("TelaStream", f"{people_counter} pessoa detectada"))
        else:
            self.label_pessoas_detectadas.setText(_translate("TelaStream", f"{people_counter} pessoas detectadas"))




    def retranslateUi(self, TelaStream):
        _translate = QtCore.QCoreApplication.translate
        TelaStream.setWindowTitle(_translate("TelaStream", "MainWindow"))
        self.radioButton.setText(_translate("TelaStream", "Emitir alerta ao detectar"))
        self.btn_voltar.setText(_translate("TelaStream", "Voltar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TelaStream()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())