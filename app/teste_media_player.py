import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QSlider, QLabel, QStyle, QSizePolicy, QHBoxLayout
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)

        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_pause)

        self.load_button = QPushButton("Load Video")
        self.load_button.clicked.connect(self.open_file)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderReleased.connect(self.slider_released)  # Connect the slider's sliderReleased signal to a function
        self.slider.sliderMoved.connect(self.set_position)

        self.label_duration = QLabel()
        self.label_duration.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        self.label_slider_text = QLabel("Slider Released: 0 seconds")

        control_layout = QHBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.addWidget(self.load_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.slider)
        control_layout.addWidget(self.label_duration)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addLayout(control_layout)
        layout.addWidget(self.label_slider_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.media_player.stateChanged.connect(self.update_buttons)
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.update_duration)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv);;All Files (*)", options=options)

        print(file_name)
        
        if file_name:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.media_player.play()

    def play_pause(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def update_buttons(self, state):
        if state == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def update_slider(self, position):
        self.slider.setValue(position)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_duration(self, duration):
        self.slider.setRange(0, duration)
        duration_in_seconds = duration / 1000
        self.label_duration.setText(f"Duration: {duration_in_seconds:.2f} seconds")

    def slider_released(self):
        seconds = self.slider.value() / 1000
        self.label_slider_text.setText(f"Slider Released: {seconds:.2f} seconds")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
