import sys
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Video Player")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100, 100, 640, 480)
        self.setupUi()

    def setupUi(self):
        self.video_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.video_player.setVideoOutput(self.video_widget)
        self.video_widget.show()
        self.playlist = QMediaPlaylist(self.video_player)
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.video_player.setPlaylist(self.playlist)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.playVideo)
        self.timer.start()

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        file_path = '/home/nomevini/Documentos/Iniciação Cientifica/Projeto/tracking_people_in_videos/app/src/windows/example.mp4'

        self.playlist.clear()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.video_player.play()

    def playVideo(self):
        if self.playlist.isEmpty():
            return

        # verifica se o vídeo atual chegou ao fim
        if self.video_player.duration() > 0 and self.video_player.position() >= self.video_player.duration() - 1000:
            self.video_player.setPosition(0)

        self.video_player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
