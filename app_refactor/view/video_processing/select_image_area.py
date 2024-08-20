from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QFont
from PyQt5.QtCore import Qt, QPoint, QSize
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB

class WindowSelectArea(QMainWindow):
    def __init__(self, file_path, MainWindow):
        super().__init__(MainWindow)
        self.file_path = file_path
        self.origin = QPoint()
        self.end = QPoint()
        
        self.coordinates = {} # guardar as cordenadas do retangulo

        self.qpixmap = self.open_file()

        # titulo da janela
        self.setWindowTitle('Selecione a área de rastreio')

        self.label = QLabel(self)
        

        self.button = QPushButton('Rastrear', self)
        self.button.setMinimumSize(QSize(460, 50))
        self.button.setMaximumSize(QSize(460, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setMouseTracking(True)
        self.button.setStyleSheet("QPushButton{\n"
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

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button, 0, Qt.AlignHCenter)

        self.label.setPixmap(self.qpixmap)
        self.label.setFixedSize(self.qpixmap.width(), self.qpixmap.height())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # fechar a janela
    def exit(self):
        QApplication.quit()

    def open_file(self):
        cap = VideoCapture(self.file_path) # Abrir o vídeo
        ret, frame = cap.read() # Ler o primeiro frame

        # Verificar se o frame foi lido corretamente
        if not ret:
            raise Exception(f"Não foi possível ler o primeiro frame do arquivo {self.file_path}")

        frame = cvtColor(frame, COLOR_BGR2RGB)

        # Cria um objeto QImage a partir do frame
        h, w, ch = frame.shape
        qimage = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)

        # Cria um objeto QPixmap a partir do QImage
        qpixmap = QPixmap.fromImage(qimage)

        cap.release() # Fechar o vídeo
        return qpixmap # Retornar o objeto QPixmap

    def clear_selection(self):
        self.origin = QPoint()
        self.end = QPoint()
        self.label.setPixmap(self.qpixmap)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clear_selection() # Limpa a seleção anterior
            self.origin = event.pos()
            self.end = event.pos()
            self.update()
        
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.end = event.pos()
            self.update() 

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end = event.pos()
            self.update()
            x1 = min(self.origin.x(), self.end.x())
            y1 = min(self.origin.y(), self.end.y())
            x2 = max(self.origin.x(), self.end.x())
            y2 = max(self.origin.y(), self.end.y())
            
            self.coordinates = {
                'x': {
                    'min': x1,
                    'max': x2
                },
                'y': {
                    'min': y1,
                    'max': y2
                }
            }
    
    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.origin.isNull() and not self.end.isNull():
            pixmap = self.qpixmap.copy()
            painter = QPainter(pixmap)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))

            # Verifica se a seleção ultrapassa as bordas da imagem
            x1 = max(min(self.origin.x(), self.end.x() + 10), 0)
            y1 = max(min(self.origin.y(), self.end.y() + 10), 0)
            x2 = min(max(self.origin.x(), self.end.x() - 10), pixmap.width() - 1)
            y2 = min(max(self.origin.y(), self.end.y() - 10), pixmap.height() - 1)

            painter.drawRect(x1, y1, x2 - x1, y2 - y1)
            painter.end()

            self.label.setPixmap(pixmap)
