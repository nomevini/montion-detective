from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.setCentralWidget(self.label)
        self.file_path = None
        self.origin = QPoint()
        self.end = QPoint()

        # Abrir uma caixa de diálogo para selecionar um arquivo de imagem
        self.open_file_dialog()

    def open_file_dialog(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Selecione uma imagem", "", "Arquivos de imagem (*.png *.jpeg *.jpg *.bmp)")

        if self.file_path:
            self.load_image()

    def load_image(self):
        pixmap = QPixmap(self.file_path)
        self.label.setPixmap(pixmap)
        self.setFixedSize(pixmap.width(), pixmap.height())

    def clear_selection(self):
        self.origin = QPoint()
        self.end = QPoint()
        self.label.setPixmap(QPixmap(self.file_path))

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
            print(f"Coordenadas do retângulo: ({x1}, {y1}), ({x2}, {y2})")

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.origin.isNull() and not self.end.isNull():
            pixmap = QPixmap(self.file_path)
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



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()