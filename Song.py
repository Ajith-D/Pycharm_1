import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMessageBox
from PyQt6.QtCore import Qt
import random
import pygame

# Sample song data
songs = [
    {"title": "Song 1", "artist": "Artist 1", "file": r"C:\Users\User\Desktop\course\Song\Journey-MassTamilan.fm.mp3"},
    {"title": "Song 2", "artist": "Artist 2", "file": r"C:\Users\User\Desktop\course\Song\Moongil Kaadugale.mp3"},
    {"title": "Song 3", "artist": "Artist 3", "file": r"C:\Users\User\Desktop\course\Song\Master-the-Blaster.mp3"},
    {"title": "Song 4", "artist": "Artist 4", "file": r"C:\Users\User\Desktop\course\Song\Thangame.mp3"},
    {"title": "Song 5", "artist": "Artist 5", "file": r"C:\Users\User\Desktop\course\Song\Daavuya.mp3"},
]

class SongRecommenderChatbot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Song Recommender Chatbot")
        self.setGeometry(300, 300, 400, 300)

        self.label = QLabel("Welcome to the Song Recommender Chatbot!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_recommend = QPushButton("Recommend Song")
        self.button_recommend.clicked.connect(self.recommend_song)

        self.button_play = QPushButton("Play Song")
        self.button_play.setEnabled(False)
        self.button_play.clicked.connect(self.play_song)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_recommend)
        layout.addWidget(self.button_play)
        layout.addWidget(self.text_edit)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.current_song = None

    def recommend_song(self):
        self.current_song = random.choice(songs)
        title = self.current_song["title"]
        artist = self.current_song["artist"]

        self.text_edit.append("Chatbot: I recommend the song:")
        self.text_edit.append(f"Title: {title}")
        self.text_edit.append(f"Artist: {artist}")
        self.text_edit.append("\n")

        self.button_play.setEnabled(True)

    def play_song(self):
        if self.current_song:
            song_file = self.current_song["file"]

            pygame.mixer.init()
            pygame.mixer.music.load(song_file)
            pygame.mixer.music.play()

    def closeEvent(self, event):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)

    window = SongRecommenderChatbot()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
