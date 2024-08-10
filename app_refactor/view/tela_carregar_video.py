from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from resources import create_rc


class Ui_TelaCarregarVideo(object):
    def setupUi(self, TelaCarregarVideo):
        TelaCarregarVideo.setObjectName("TelaCarregarVideo")
        TelaCarregarVideo.resize(1147, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TelaCarregarVideo.sizePolicy().hasHeightForWidth())
        TelaCarregarVideo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        TelaCarregarVideo.setFont(font)
        TelaCarregarVideo.setAutoFillBackground(False)
        TelaCarregarVideo.setStyleSheet("background-color: rgb(33, 46, 46);")
        self.centralwidget = QtWidgets.QWidget(TelaCarregarVideo)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_video = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_video.sizePolicy().hasHeightForWidth())
        self.frame_video.setSizePolicy(sizePolicy)
        self.frame_video.setMaximumSize(QtCore.QSize(16777215, 800))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_video.setFont(font)
        self.frame_video.setStyleSheet("padding-left: 20px;\n"
"border: none")
        self.frame_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_video.setObjectName("frame_video")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_video)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame_1 = QtWidgets.QFrame(self.frame_video)
        self.frame_1.setEnabled(True)
        self.frame_1.setMinimumSize(QtCore.QSize(600, 580))
        self.frame_1.setStyleSheet("border: none")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_1)
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.label_selecionar_video = QtWidgets.QLabel(self.frame_1)
        self.label_selecionar_video.setMinimumSize(QtCore.QSize(0, 50))
        self.label_selecionar_video.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_selecionar_video.setFont(font)
        self.label_selecionar_video.setMouseTracking(False)
        self.label_selecionar_video.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_selecionar_video.setWhatsThis("")
        self.label_selecionar_video.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 0px;")
        self.label_selecionar_video.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_selecionar_video.setObjectName("label_selecionar_video")
        self.verticalLayout_4.addWidget(self.label_selecionar_video)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_nome_arquivo = QtWidgets.QLabel(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome_arquivo.sizePolicy().hasHeightForWidth())
        self.label_nome_arquivo.setSizePolicy(sizePolicy)
        self.label_nome_arquivo.setMinimumSize(QtCore.QSize(400, 60))
        self.label_nome_arquivo.setMaximumSize(QtCore.QSize(400, 60))
        self.label_nome_arquivo.setStyleSheet("background: #212E2E;\n"
"border: 2px solid #445858;\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;"
"margin-bottom: 10px;")
        self.label_nome_arquivo.setObjectName("label_nome_arquivo")
        self.horizontalLayout_4.addWidget(self.label_nome_arquivo, 0, QtCore.Qt.AlignLeft)
        self.pushButton_carregar_video = QtWidgets.QPushButton(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_carregar_video.sizePolicy().hasHeightForWidth())
        self.pushButton_carregar_video.setSizePolicy(sizePolicy)
        self.pushButton_carregar_video.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_carregar_video.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_carregar_video.setMouseTracking(True)
        self.pushButton_carregar_video.setToolTipDuration(-1)
        self.pushButton_carregar_video.setStatusTip("")
        self.pushButton_carregar_video.setWhatsThis("")
        self.pushButton_carregar_video.setAccessibleName("")
        self.pushButton_carregar_video.setAccessibleDescription("")
        self.pushButton_carregar_video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_carregar_video.setStyleSheet("\n"
"QPushButton {\n"
"    image: url(:/file_load/file.png);\n"
"    padding-left: 15px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    image: url(:/file_load/file-hover.png)\n"
"}\n"
"\n"
"\n"
"QToolTip{\n"
"    padding: 2px;\n"
"}")
        self.pushButton_carregar_video.setText("")
        self.pushButton_carregar_video.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_carregar_video.setDefault(False)
        self.pushButton_carregar_video.setFlat(True)
        self.pushButton_carregar_video.setObjectName("pushButton_carregar_video")
        self.horizontalLayout_4.addWidget(self.pushButton_carregar_video, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.checkBox_reduzir_dimensao = QtWidgets.QCheckBox(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_reduzir_dimensao.sizePolicy().hasHeightForWidth())
        self.checkBox_reduzir_dimensao.setSizePolicy(sizePolicy)
        self.checkBox_reduzir_dimensao.setMinimumSize(QtCore.QSize(0, 50))
        self.checkBox_reduzir_dimensao.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_reduzir_dimensao.setFont(font)
        self.checkBox_reduzir_dimensao.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    width: 50px;\n"
"    height: 50px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(:/checkbox/checbox_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/checkbox/checbox_enable.png);\n"
"}\n"
"\n"
"\n"
"QToolTip{\n"
"    padding: 2px;\n"
"}")
        self.checkBox_reduzir_dimensao.setObjectName("checkBox_reduzir_dimensao")
        self.verticalLayout_4.addWidget(self.checkBox_reduzir_dimensao)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_dimensao_1 = QtWidgets.QLineEdit(self.frame_1)
        self.lineEdit_dimensao_1.setEnabled(True)
        self.lineEdit_dimensao_1.setMinimumSize(QtCore.QSize(10, 40))
        self.lineEdit_dimensao_1.setMaximumSize(QtCore.QSize(90, 40))
        self.lineEdit_dimensao_1.setStyleSheet("QLineEdit{\n"
"    background: #212E2E;\n"
"    border: 2px solid #445858;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(171, 171, 171);\n"
"}")
        self.lineEdit_dimensao_1.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_dimensao_1.setInputMask("")
        self.lineEdit_dimensao_1.setText("")
        self.lineEdit_dimensao_1.setObjectName("lineEdit_dimensao_1")
        self.horizontalLayout_3.addWidget(self.lineEdit_dimensao_1)
        self.label_x = QtWidgets.QLabel(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy)
        self.label_x.setMaximumSize(QtCore.QSize(40, 40))
        self.label_x.setSizeIncrement(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_x.setFont(font)
        self.label_x.setStyleSheet("color: rgb(68, 88, 88);\n"
"margin: 10 10 10 10;\n"
"border: none;\n"
"padding: 0;")
        self.label_x.setObjectName("label_x")
        self.horizontalLayout_3.addWidget(self.label_x)
        self.lineEdit_dimensao_2 = QtWidgets.QLineEdit(self.frame_1)
        self.lineEdit_dimensao_2.setEnabled(True)
        self.lineEdit_dimensao_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_dimensao_2.setMaximumSize(QtCore.QSize(90, 40))
        self.lineEdit_dimensao_2.setStyleSheet("QLineEdit{\n"
"    background: #212E2E;\n"
"    border: 2px solid #445858;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(171, 171, 171);\n"
"}")
        self.lineEdit_dimensao_2.setObjectName("lineEdit_dimensao_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_dimensao_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.label_erro_dimensao = QtWidgets.QLabel(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_erro_dimensao.sizePolicy().hasHeightForWidth())
        self.label_erro_dimensao.setSizePolicy(sizePolicy)
        self.label_erro_dimensao.setMinimumSize(QtCore.QSize(550, 50))
        self.label_erro_dimensao.setMaximumSize(QtCore.QSize(550, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_erro_dimensao.setFont(font)
        self.label_erro_dimensao.setStyleSheet("color: rgb(224, 27, 36);\n"
"padding-left: 0px;")
        self.label_erro_dimensao.setObjectName("label_erro_dimensao")
        self.verticalLayout_4.addWidget(self.label_erro_dimensao)
        self.checkBox_reduzir_fps = QtWidgets.QCheckBox(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_reduzir_fps.sizePolicy().hasHeightForWidth())
        self.checkBox_reduzir_fps.setSizePolicy(sizePolicy)
        self.checkBox_reduzir_fps.setMinimumSize(QtCore.QSize(0, 50))
        self.checkBox_reduzir_fps.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_reduzir_fps.setFont(font)
        self.checkBox_reduzir_fps.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    width: 50px;\n"
"    height: 50px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(:/checkbox/checbox_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/checkbox/checbox_enable.png);\n"
"}\n"
"\n"
"\n"
"QToolTip{\n"
"    padding: 2px;\n"
"}")
        self.checkBox_reduzir_fps.setObjectName("checkBox_reduzir_fps")
        self.verticalLayout_4.addWidget(self.checkBox_reduzir_fps)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_fps = QtWidgets.QLineEdit(self.frame_1)
        self.lineEdit_fps.setMinimumSize(QtCore.QSize(90, 40))
        self.lineEdit_fps.setMaximumSize(QtCore.QSize(90, 40))
        self.lineEdit_fps.setStyleSheet("QLineEdit{\n"
"    background: #212E2E;\n"
"    border: 2px solid #445858;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(171, 171, 171);\n"
"}")
        self.lineEdit_fps.setObjectName("lineEdit_fps")
        self.horizontalLayout_5.addWidget(self.lineEdit_fps)
        self.label_fps = QtWidgets.QLabel(self.frame_1)
        self.label_fps.setMinimumSize(QtCore.QSize(0, 40))
        self.label_fps.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_fps.setStyleSheet("padding-left: 10px;\n"
"color: rgb(255, 255, 255);")
        self.label_fps.setObjectName("label_fps")
        self.horizontalLayout_5.addWidget(self.label_fps)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.label_erro_fps = QtWidgets.QLabel(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_erro_fps.sizePolicy().hasHeightForWidth())
        self.label_erro_fps.setSizePolicy(sizePolicy)
        self.label_erro_fps.setMinimumSize(QtCore.QSize(0, 50))
        self.label_erro_fps.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_erro_fps.setFont(font)
        self.label_erro_fps.setStyleSheet("color: rgb(224, 27, 36);\n"
"padding-left: 0px;")
        self.label_erro_fps.setObjectName("label_erro_fps")
        self.verticalLayout_4.addWidget(self.label_erro_fps)
        self.checkBox_analise_frame_a_frame = QtWidgets.QCheckBox(self.frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_analise_frame_a_frame.sizePolicy().hasHeightForWidth())
        self.checkBox_analise_frame_a_frame.setSizePolicy(sizePolicy)
        self.checkBox_analise_frame_a_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.checkBox_analise_frame_a_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_analise_frame_a_frame.setFont(font)
        self.checkBox_analise_frame_a_frame.setStyleSheet("QCheckBox{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    width: 50px;\n"
"    height: 50px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"    image: url(:/checkbox/checbox_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/checkbox/checbox_enable.png);\n"
"}\n"
"\n"
"\n"
"QToolTip{\n"
"    padding: 2px;\n"
"}")
        self.checkBox_analise_frame_a_frame.setObjectName("checkBox_analise_frame_a_frame")
        self.verticalLayout_4.addWidget(self.checkBox_analise_frame_a_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/eye/eyeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.label_erro_area_rastreio = QtWidgets.QLabel(self.frame_1)
        self.label_erro_area_rastreio.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_erro_area_rastreio.sizePolicy().hasHeightForWidth())
        self.label_erro_area_rastreio.setSizePolicy(sizePolicy)
        self.label_erro_area_rastreio.setMinimumSize(QtCore.QSize(0, 50))
        self.label_erro_area_rastreio.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_erro_area_rastreio.setFont(font)
        self.label_erro_area_rastreio.setStyleSheet("color: rgb(224, 27, 36);\n"
"padding-left: 0px;")
        self.label_erro_area_rastreio.setObjectName("label_erro_area_rastreio")
        self.verticalLayout_4.addWidget(self.label_erro_area_rastreio)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.frame_1)
        self.frame_2 = QtWidgets.QFrame(self.frame_video)
        self.frame_2.setStyleSheet("border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_image = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_image.sizePolicy().hasHeightForWidth())
        self.frame_image.setSizePolicy(sizePolicy)
        self.frame_image.setMinimumSize(QtCore.QSize(400, 250))
        self.frame_image.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_image.setStyleSheet("margin-bottom: 10px;")
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_image)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_image)
        self.label_7.setMinimumSize(QtCore.QSize(400, 230))
        self.label_7.setMaximumSize(QtCore.QSize(400, 230))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.verticalLayout_2.addWidget(self.frame_image)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_3.setToolTip("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setContentsMargins(0, 0, -1, 9)
        self.formLayout.setObjectName("formLayout")
        self.label_video_info = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_video_info.setFont(font)
        self.label_video_info.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 0px;")
        self.label_video_info.setObjectName("label_video_info")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_video_info)
        self.label_nome_do_arquivo = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nome_do_arquivo.sizePolicy().hasHeightForWidth())
        self.label_nome_do_arquivo.setSizePolicy(sizePolicy)
        self.label_nome_do_arquivo.setMinimumSize(QtCore.QSize(155, 30))
        self.label_nome_do_arquivo.setMaximumSize(QtCore.QSize(155, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_nome_do_arquivo.setFont(font)
        self.label_nome_do_arquivo.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 0px;")
        self.label_nome_do_arquivo.setObjectName("label_nome_do_arquivo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_nome_do_arquivo)
        self.label_rsp_nome_do_arquivo = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rsp_nome_do_arquivo.sizePolicy().hasHeightForWidth())
        self.label_rsp_nome_do_arquivo.setSizePolicy(sizePolicy)
        self.label_rsp_nome_do_arquivo.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_rsp_nome_do_arquivo.setFont(font)
        self.label_rsp_nome_do_arquivo.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-left: 1px;")
        self.label_rsp_nome_do_arquivo.setObjectName("label_rsp_nome_do_arquivo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_rsp_nome_do_arquivo)
        self.label_dimensao = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dimensao.sizePolicy().hasHeightForWidth())
        self.label_dimensao.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_dimensao.setFont(font)
        self.label_dimensao.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 0px;")
        self.label_dimensao.setObjectName("label_dimensao")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_dimensao)
        self.label_rsp_dimensao = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_rsp_dimensao.setFont(font)
        self.label_rsp_dimensao.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 1px;")
        self.label_rsp_dimensao.setObjectName("label_rsp_dimensao")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_rsp_dimensao)
        self.label_tamanho = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tamanho.sizePolicy().hasHeightForWidth())
        self.label_tamanho.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_tamanho.setFont(font)
        self.label_tamanho.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 0px;")
        self.label_tamanho.setObjectName("label_tamanho")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_tamanho)
        self.label_rsp_tamanho = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_rsp_tamanho.setFont(font)
        self.label_rsp_tamanho.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding: 1px;")
        self.label_rsp_tamanho.setObjectName("label_rsp_tamanho")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_rsp_tamanho)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame_video, 0, QtCore.Qt.AlignHCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem7)
        self.label_erro_video_nao_selecionado = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_erro_video_nao_selecionado.sizePolicy().hasHeightForWidth())
        self.label_erro_video_nao_selecionado.setSizePolicy(sizePolicy)
        self.label_erro_video_nao_selecionado.setMinimumSize(QtCore.QSize(0, 50))
        self.label_erro_video_nao_selecionado.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_erro_video_nao_selecionado.setFont(font)
        self.label_erro_video_nao_selecionado.setStyleSheet("color: rgb(224, 27, 36);")
        self.label_erro_video_nao_selecionado.setObjectName("label_erro_video_nao_selecionado")
        self.verticalLayout.addWidget(self.label_erro_video_nao_selecionado, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_rastrear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rastrear.setMinimumSize(QtCore.QSize(460, 50))
        self.pushButton_rastrear.setMaximumSize(QtCore.QSize(460, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rastrear.setFont(font)
        self.pushButton_rastrear.setMouseTracking(True)
        self.pushButton_rastrear.setStyleSheet("QPushButton{\n"
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
"QToolTip{\n"
"    padding: 2px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_rastrear.setObjectName("pushButton_rastrear")
        self.verticalLayout.addWidget(self.pushButton_rastrear, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_voltar.sizePolicy().hasHeightForWidth())
        self.pushButton_voltar.setSizePolicy(sizePolicy)
        self.pushButton_voltar.setMinimumSize(QtCore.QSize(460, 50))
        self.pushButton_voltar.setMaximumSize(QtCore.QSize(460, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setStyleSheet("QPushButton{\n"
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
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.verticalLayout.addWidget(self.pushButton_voltar, 0, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        TelaCarregarVideo.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaCarregarVideo)
        QtCore.QMetaObject.connectSlotsByName(TelaCarregarVideo)

        int_validator = QIntValidator()

        self.lineEdit_dimensao_1.setValidator(int_validator)
        self.lineEdit_dimensao_2.setValidator(int_validator)
        self.lineEdit_fps.setValidator(int_validator)

        # desativar os labels de alerta
        self.label_erro_dimensao.setVisible(False)
        self.label_erro_fps.setVisible(False)
        self.label_erro_area_rastreio.setVisible(False)
        self.label_erro_video_nao_selecionado.setVisible(False)

        # desativar os campos de entrada dos checkbox
        self.lineEdit_dimensao_1.setVisible(False)
        self.lineEdit_dimensao_2.setVisible(False)
        self.lineEdit_fps.setVisible(False)
        self.label_x.setVisible(False)
        self.label_fps.setVisible(False)

    def retranslateUi(self, TelaCarregarVideo):
        _translate = QtCore.QCoreApplication.translate
        TelaCarregarVideo.setWindowTitle(_translate("TelaCarregarVideo", "MainWindow"))
        self.label_selecionar_video.setText(_translate("TelaCarregarVideo", "Selecionar video"))
        self.label_nome_arquivo.setText(_translate("TelaCarregarVideo", ""))
        self.pushButton_carregar_video.setToolTip(_translate("TelaCarregarVideo", "<html><head/><body><p><span style=\" color:#ffffff;\">Carregar video</span></p></body></html>"))
        self.checkBox_reduzir_dimensao.setToolTip(_translate("TelaCarregarVideo", "<html><head/><body><p><span style=\" color:#ffffff;\">Reduz a resolução do vídeo, o que pode melhorar significativamente a velocidade de processamento. Isso é útil para vídeos grandes ou para computadores com recursos limitados.</span></p></body></html>"))
        self.checkBox_reduzir_dimensao.setText(_translate("TelaCarregarVideo", "Reduzir dimensão do video"))
        self.label_x.setText(_translate("TelaCarregarVideo", "X"))
        self.label_erro_dimensao.setText(_translate("TelaCarregarVideo", "Dimensão inválida"))
        self.checkBox_reduzir_fps.setToolTip(_translate("TelaCarregarVideo", "<html><head/><body><p align=\"justify\"><span style=\" color:#ffffff;\">Reduzir a quantidade de frames por segundo do vídeo. </span></p><p align=\"justify\"><span style=\" color:#ffffff;\">A redução é ideal para melhorar o processamento e reduzir o custo computacional</span></p></body></html>"))
        self.checkBox_reduzir_fps.setText(_translate("TelaCarregarVideo", "Reduzir FPS"))
        self.label_fps.setText(_translate("TelaCarregarVideo", "FPS"))
        self.label_erro_fps.setText(_translate("TelaCarregarVideo", "O FPS digitado é maior que o do vídeo original"))
        self.checkBox_analise_frame_a_frame.setToolTip(_translate("TelaCarregarVideo", "<html><head/><body><p align=\"justify\"><span style=\" color:#ffffff;\">Essa função salva todos os rastreamentos de pessoas em todos os quadros de um vídeo. </span></p><p align=\"justify\"><span style=\" color:#ffffff;\">OBS: Essa operação pode aumentar significativamente o consumo de memória.</span></p></body></html>"))
        self.checkBox_analise_frame_a_frame.setText(_translate("TelaCarregarVideo", "Permitir analise frame a frame"))
        self.label_erro_area_rastreio.setText(_translate("TelaCarregarVideo", "O vídeo deve ser carregador antes de selecionar a área de rastreio"))
        self.label_video_info.setText(_translate("TelaCarregarVideo", "VÍDEO INFO:"))
        self.label_nome_do_arquivo.setText(_translate("TelaCarregarVideo", "Nome do arquivo: "))
        self.label_rsp_nome_do_arquivo.setText(_translate("TelaCarregarVideo", "Some video.mp4"))
        self.label_dimensao.setText(_translate("TelaCarregarVideo", "Dimensão:"))
        self.label_rsp_dimensao.setText(_translate("TelaCarregarVideo", "1366x768 px"))
        self.label_tamanho.setText(_translate("TelaCarregarVideo", "Tamanho"))
        self.label_rsp_tamanho.setText(_translate("TelaCarregarVideo", "450 kb"))
        self.label_erro_video_nao_selecionado.setText(_translate("TelaCarregarVideo", "O vídeo não foi selecionado"))
        self.pushButton_rastrear.setToolTip(_translate("TelaCarregarVideo", "<html><head/><body><p><span style=\" color:#ffffff;\">Iniciar o rastreamento de pessoas</span></p></body></html>"))
        self.pushButton_rastrear.setText(_translate("TelaCarregarVideo", "Rastrear"))
        self.pushButton_voltar.setToolTip(_translate("TelaCarregarVideo", "<html><head/><body><p><span style=\" color:#ffffff;\">Volta a tela inicial</span></p></body></html>"))
        self.pushButton_voltar.setText(_translate("TelaCarregarVideo", "Voltar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCarregarVideo = QtWidgets.QMainWindow()
    ui = Ui_TelaCarregarVideo()
    ui.setupUi(TelaCarregarVideo)
    TelaCarregarVideo.show()
    sys.exit(app.exec_())
