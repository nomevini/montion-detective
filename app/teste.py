from PyQt5.QtCore import QThread, pyqtSignal, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget


class SecondThread(QThread):
    finished = pyqtSignal()  # Sinal para notificar a thread principal

    def run(self):
        # Coloque aqui o código da segunda thread
        # Esta função será executada em uma nova thread

        # Exemplo: Aguarde 5 segundos
        import time
        time.sleep(5)

        self.finished.emit()  # Emite o sinal quando a segunda thread terminar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de Comunicação entre Threads")
        self.layout = QVBoxLayout()

        self.label = QLabel("Aguardando término da segunda thread...", self)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Iniciar Segunda Thread", self)
        self.button.clicked.connect(self.iniciar_segunda_thread)
        self.layout.addWidget(self.button)

        self.widget = QWidget(self)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def iniciar_segunda_thread(self):
        self.button.setEnabled(False)
        self.label.setText("Segunda thread em execução...")

        # Inicia a segunda thread
        self.second_thread = SecondThread()
        self.second_thread.finished.connect(self.second_thread_terminada)
        self.second_thread.start()

    def second_thread_terminada(self):
        self.label.setText("Segunda thread terminada!")
        self.button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
