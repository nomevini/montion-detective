from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaVideoEntrada(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1189, 671)
        MainWindow.setMinimumSize(QtCore.QSize(0, 671))
        MainWindow.setStyleSheet("background-color: rgb(33, 46, 46);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Label "Selecionar Dispositivo"
        self.label_selecionar_dispositivo = QtWidgets.QLabel(self.centralwidget)
        self.label_selecionar_dispositivo.setObjectName("label_selecionar_dispositivo")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_selecionar_dispositivo.setFont(font)
        self.label_selecionar_dispositivo.setStyleSheet("color: white; margin-bottom: 20px; margin-top:10px;")
        self.label_selecionar_dispositivo.setText("Selecionar Dispositivo")
        self.verticalLayout.addWidget(self.label_selecionar_dispositivo)

        # Layout horizontal para os radio buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Radio buttons
        self.radioButton_webcam = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_webcam.setObjectName("radioButton_webcam")
        self.radioButton_webcam.setText("Webcam")
        self.radioButton_webcam.setChecked(True)
        self.radioButton_webcam.toggled.connect(self.selection_changed)  # Connect selection_changed slot
        self.radioButton_webcam.setStyleSheet("""
            QRadioButton {
                color: white;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                border: 3px solid white;
            }
            QRadioButton::indicator:checked {
                background-color: white;
            }
        """)
        self.horizontalLayout.addWidget(self.radioButton_webcam)

        self.radioButton_intelbras = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_intelbras.setObjectName("radioButton_intelbras")
        self.radioButton_intelbras.setText("Intelbras")
        self.radioButton_intelbras.toggled.connect(self.selection_changed)  # Connect selection_changed slot
        self.radioButton_intelbras.setStyleSheet("""
            QRadioButton {
                color: white;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                border: 3px solid white;
            }
            QRadioButton::indicator:checked {
                background-color: white;
            }
        """)
        self.horizontalLayout.addWidget(self.radioButton_intelbras)

        # Adicionar layout horizontal ao layout vertical
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setObjectName("user_label")
        self.user_label.setStyleSheet("color: white; font-size: 16px;")
        self.verticalLayout.addWidget(self.user_label)
        self.user_label.setVisible(False)

        self.user_input = QtWidgets.QLineEdit(self.centralwidget)
        self.user_input.setObjectName("user_input")
        self.user_input.setStyleSheet("color: white; background-color: rgb(50, 50, 50); border: 1px solid white; min-width: 200px; min-height: 40px; font-size: 18px")
        self.verticalLayout.addWidget(self.user_input)
        self.user_input.setVisible(False)
        
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setObjectName("pass_label")
        self.pass_label.setStyleSheet("color: white; font-size: 16px;")
        self.verticalLayout.addWidget(self.pass_label)
        self.pass_label.setVisible(False)
        
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setObjectName("pass_input")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setStyleSheet("color: white; background-color: rgb(50, 50, 50); border: 1px solid white; min-width: 200px;  min-height: 40px; font-size: 18px")
        self.verticalLayout.addWidget(self.pass_input)
        self.pass_input.setVisible(False)
        
        self.channel_label = QtWidgets.QLabel(self.centralwidget)
        self.channel_label.setObjectName("channel_label")
        self.channel_label.setStyleSheet("color: white; font-size: 16px;")
        self.verticalLayout.addWidget(self.channel_label)
        self.channel_label.setVisible(False)
        
        self.channel_input = QtWidgets.QLineEdit(self.centralwidget)
        self.channel_input.setObjectName("channel_input")
        self.channel_input.setStyleSheet("color: white; background-color: rgb(50, 50, 50); border: 1px solid white; min-width: 200px; min-height: 40px; font-size: 18px")
        self.verticalLayout.addWidget(self.channel_input)
        self.channel_input.setVisible(False)

        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setObjectName("channel_label")
        self.ip_label.setStyleSheet("color: white; font-size: 16px;")
        self.verticalLayout.addWidget(self.ip_label)
        self.ip_label.setVisible(False)
        
        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_input.setObjectName("channel_input")
        self.ip_input.setStyleSheet("color: white; background-color: rgb(50, 50, 50); border: 1px solid white; min-width: 200px; min-height: 40px; font-size: 18px")
        self.verticalLayout.addWidget(self.ip_input)
        self.ip_input.setVisible(False)

        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.track_button = QtWidgets.QPushButton(self.centralwidget)
        self.track_button.setMinimumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.track_button.setFont(font)
        self.track_button.setStyleSheet("QPushButton{\n"
"    background: #552D96;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
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
        self.track_button.setObjectName("track_button")
        self.verticalLayout.addWidget(self.track_button)
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(330, 50))
        self.back_button.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: white;")
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)

        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_label.setText(_translate("MainWindow", "Usuário:"))
        self.pass_label.setText(_translate("MainWindow", "Senha:"))
        self.channel_label.setText(_translate("MainWindow", "Canal da câmera:"))
        self.ip_label.setText(_translate("MainWindow", "IP da câmera:"))
        self.track_button.setText(_translate("MainWindow", "Rastrear"))
        self.back_button.setText(_translate("MainWindow", "Voltar"))
        self.radioButton_webcam.setText(_translate("MainWindow", "Webcam"))
        self.radioButton_intelbras.setText(_translate("MainWindow", "Câmera Intelbras"))
        self.label_selecionar_dispositivo.setText(_translate("MainWindow", "Selecionar Dispositivo"))

    def selection_changed(self):
        if self.radioButton_intelbras.isChecked():  # Intelbras selected
            self.user_label.setVisible(True)
            self.user_input.setVisible(True)
            self.pass_label.setVisible(True)
            self.pass_input.setVisible(True)
            self.channel_label.setVisible(True)
            self.channel_input.setVisible(True)
            self.ip_label.setVisible(True)
            self.ip_input.setVisible(True)
        else:  # Webcam selected
            self.user_label.setVisible(False)
            self.user_input.setVisible(False)
            self.pass_label.setVisible(False)
            self.pass_input.setVisible(False)
            self.channel_label.setVisible(False)
            self.channel_input.setVisible(False)
            self.ip_label.setVisible(False)
            self.ip_input.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaInicial = QtWidgets.QMainWindow()
    ui = Ui_TelaVideoEntrada()
    ui.setupUi(TelaInicial)
    TelaInicial.show()
    sys.exit(app.exec_())
