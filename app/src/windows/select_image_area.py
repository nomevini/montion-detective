from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QFont
from PyQt5.QtCore import Qt, QPoint, QSize
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB

class WindowSelectArea(QMainWindow):
    def __init__(self, file_path, MainWindow):
        super().__init__(MainWindow)
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.file_path = file_path
        self.origin = QPoint()
        self.end = QPoint()
        self.qpixmap = self.open_file()
        self.coordinates = {} # guardar as cordenadas do retangulo

        # Botão Rastrear
        self.button = QPushButton("Rastrear", self)
        self.button.setMinimumSize(QSize(460, 50))
        self.button.setMaximumSize(QSize(460, 50))
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
        #button.clicked.connect(self.rastrear)

        # Layout Vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button,  0, Qt.AlignHCenter)
        
        # Widget para o layout
        widget = QWidget(self)
        widget.setLayout(layout)

        # Adicionar o widget ao layout central da janela
        self.setCentralWidget(widget)


        # titulo da janela
        self.setWindowTitle('Selecione a área de rastreio')

        self.load_image()        
        
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
        bytes_per_line = ch * w
        qimage = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # Cria um objeto QPixmap a partir do QImage
        qpixmap = QPixmap.fromImage(qimage)

        cap.release() # Fechar o vídeo
        return qpixmap # Retornar o objeto QPixmap

    def load_image(self):
        self.label.setPixmap(self.qpixmap)
        self.setFixedSize(self.qpixmap.width(), self.qpixmap.height())

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
            ##self.exit()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.origin.isNull() and not self.end.isNull():
            pixmap = self.qpixmap.copy()
            painter = QPainter(pixmap)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))

            # Verifica se a seleção ultrapassa as bordas da imagem
            x1 = max(min(self.origin.x(), self.end.x() - 10), 0)
            y1 = max(min(self.origin.y(), self.end.y() + int(self.button.height()/2)), 0)
            x2 = min(max(self.origin.x(), self.end.x() - 10), pixmap.width() - 1)
            y2 = min(max(self.origin.y(), self.end.y() + int(self.button.height()/2)), pixmap.height() - 1)

            painter.drawRect(x1, y1, x2 - x1, y2 - y1)
            painter.end()

            # Copia o pixmap temporário para o pixmap original da QLabel
            self.label.setPixmap(pixmap)

        