from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QTimer, QUrl
import os

class Ui_TelaInicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("TelaInicial")
        MainWindow.resize(1177, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(33, 46, 46);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(960, 16777215))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.video = QVideoWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy)
        self.video.setMinimumSize(QtCore.QSize(640, 330))
        self.video.setMaximumSize(QtCore.QSize(640, 360))
        self.video.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 30px")
        self.video.setObjectName("video")
        self.horizontalLayout_2.addWidget(self.video)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.montiondetective = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.montiondetective.sizePolicy().hasHeightForWidth())
        self.montiondetective.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.montiondetective.setFont(font)
        self.montiondetective.setStyleSheet("color: rgb(239, 239, 239);")
        self.montiondetective.setAlignment(QtCore.Qt.AlignCenter)
        self.montiondetective.setObjectName("montiondetective")
        self.verticalLayout_2.addWidget(self.montiondetective)
        self.descricao = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descricao.sizePolicy().hasHeightForWidth())
        self.descricao.setSizePolicy(sizePolicy)
        self.descricao.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.descricao.setFont(font)
        self.descricao.setStyleSheet("color: rgb(239, 239, 239);")
        self.descricao.setAlignment(QtCore.Qt.AlignCenter)
        self.descricao.setObjectName("descricao")
        self.verticalLayout_2.addWidget(self.descricao)
        self.Frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_4.sizePolicy().hasHeightForWidth())
        self.Frame_4.setSizePolicy(sizePolicy)
        self.Frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.Frame_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_4.setObjectName("Frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_video = QtWidgets.QPushButton(self.Frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_video.sizePolicy().hasHeightForWidth())
        self.btn_video.setSizePolicy(sizePolicy)
        self.btn_video.setMinimumSize(QtCore.QSize(330, 50))
        self.btn_video.setMaximumSize(QtCore.QSize(410, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_video.setFont(font)
        self.btn_video.setStyleSheet("QPushButton{\n"
"    background: #552D96;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    position: absolute;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(59, 31, 104);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.btn_video.setObjectName("btn_video")
        self.horizontalLayout_4.addWidget(self.btn_video)
        self.verticalLayout_2.addWidget(self.Frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setStyleSheet("border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_realtime = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_realtime.sizePolicy().hasHeightForWidth())
        self.btn_realtime.setSizePolicy(sizePolicy)
        self.btn_realtime.setMinimumSize(QtCore.QSize(330, 50))
        self.btn_realtime.setMaximumSize(QtCore.QSize(410, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btn_realtime.setFont(font)
        self.btn_realtime.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_realtime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_realtime.setAutoFillBackground(False)
        self.btn_realtime.setStyleSheet("QPushButton{\n"
"    background: #552D96;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    position: absolute;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(59, 31, 104);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.btn_realtime.setAutoDefault(False)
        self.btn_realtime.setDefault(False)
        self.btn_realtime.setFlat(False)
        self.btn_realtime.setObjectName("btn_realtime")
        self.horizontalLayout_3.addWidget(self.btn_realtime)
        self.verticalLayout_2.addWidget(self.frame_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.video_player = QMediaPlayer()
        self.video_player.setVideoOutput(self.video)
        self.video.show()

        self.playlist = QMediaPlaylist(self.video_player)
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.video_player.setPlaylist(self.playlist)

        self.timer = QTimer(MainWindow)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.playVideo)
        self.timer.start()

        # Capturar o diretório atual do arquivo
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Retroceder uma pasta para acessar a pasta pai
        parent_directory = os.path.dirname(current_directory)

        # Construir o caminho para o arquivo de vídeo usando um caminho relativo
        file_path = os.path.join(parent_directory, 'resources', 'example.mp4')

        self.playlist.clear()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.video_player.play()

    def playVideo(self):
        if self.playlist.isEmpty():
            return
        
    def stopVideo(self):
        self.video_player.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TelaInicial", "MainWindow"))
        self.montiondetective.setText(_translate("TelaInicial", "MONTIONDETECTIVE"))
        self.descricao.setText(_translate("TelaInicial", "Detecção e rastreio de pessoas em vídeo"))
        self.btn_video.setText(_translate("TelaInicial", "Processar Vídeo"))
        self.btn_realtime.setToolTip(_translate("TelaInicial", "<html><head/><body><p><span style=\" color:#ffffff;\">Iniciar o rastreamento de pessoas</span></p></body></html>"))
        self.btn_realtime.setText(_translate("TelaInicial", "Rastrear em tempo real"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TelaInicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())