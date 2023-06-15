import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget


class WorkerThread(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        count = 0
        while self.running:
            count += 1
            self.countChanged.emit(count)
            time.sleep(1)

    def stop(self):
        self.running = False


class ProcessThread(QThread):
    finished = pyqtSignal()

    def run(self):
        # Simulando um processo que leva tempo para ser concluído
        time.sleep(5)
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thread Example")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("0", alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.button_start = QPushButton("Start")
        self.button_start.clicked.connect(self.start_threads)
        self.layout.addWidget(self.button_start)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.worker_thread = None
        self.process_thread = None

    def start_threads(self):
        self.button_start.setEnabled(False)

        # Inicia a thread do processo
        self.process_thread = ProcessThread()
        self.process_thread.finished.connect(self.process_finished)
        self.process_thread.start()

        # Inicia a thread do contador
        self.worker_thread = WorkerThread()
        self.worker_thread.countChanged.connect(self.update_label)
        self.worker_thread.start()

    def process_finished(self):
        # Chamado quando o processo é concluído
        self.button_start.setEnabled(True)

    def update_label(self, count):
        self.label.setText(str(count))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
