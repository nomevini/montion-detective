from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QTimer, QUrl


        self.video_player = QMediaPlayer()
        self.video_player.setVideoOutput(self.widget)
        self.widget.show()

        self.playlist = QMediaPlaylist(self.video_player)
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.video_player.setPlaylist(self.playlist)

        self.timer = QTimer(TelaInicial)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.playVideo)
        self.timer.start()

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
