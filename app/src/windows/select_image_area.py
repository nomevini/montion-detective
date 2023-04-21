from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage
from PyQt5.QtCore import Qt, QPoint
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB

class WindowSelectArea(QMainWindow):
    def __init__(self, file_path):
        super().__init__()
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.file_path = file_path
        self.origin = QPoint()
        self.end = QPoint()
        self.qpixmap = self.open_file()
        self.coordinates = {} # guardar as cordenadas do retangulo

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
            self.exit()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.origin.isNull() and not self.end.isNull():
            pixmap = self.qpixmap.copy()
            painter = QPainter(pixmap)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))

            # Verifica se a seleção ultrapassa as bordas da imagem
            x1 = max(min(self.origin.x(), self.end.x()), 0)
            y1 = max(min(self.origin.y(), self.end.y()), 0)
            x2 = min(max(self.origin.x(), self.end.x()), pixmap.width() - 1)
            y2 = min(max(self.origin.y(), self.end.y()), pixmap.height() - 1)

            painter.drawRect(x1, y1, x2 - x1, y2 - y1)
            painter.end()

            self.label.setPixmap(pixmap)

def get_coordinates(video_path):
    app = QApplication([])
    window = WindowSelectArea(video_path)
    window.show()
    app.exec_()
    return window.coordinates
