import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import random
import pygame
import os

# Sample songs
song_directory = {
    "happy": r"C:\Users\User\Desktop\course\Song\Happy",
    "sad": r"C:\Users\User\Desktop\course\Song\Sad",
    "motivation": r"C:\Users\User\Desktop\course\Song\Motivation",
}

class SongRecommender(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Song Recommender Chatbot")
        self.setGeometry(300, 300, 400, 300)

        self.label = QLabel("Welcome to the Song Recommender Chatbot!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_recommend = QPushButton("Recommend Song")
        self.button_recommend.clicked.connect(self.recommend_song)
        self.button_recommend.setStyleSheet('color: black; background-color: #FFEFD5')

        self.button_play = QPushButton("Play Song")
        self.button_play.setEnabled(False)
        self.button_play.clicked.connect(self.play_song)
        self.button_play.setStyleSheet('color: white; background-color: black')

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.input_label = QLabel("Enter your mood:")
        self.input_line_edit = QLineEdit()
        self.input_line_edit.setStyleSheet('Background-color : lightgrey')
        self.input_line_edit.returnPressed.connect(self.recommend_song)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_line_edit)
        layout.addWidget(self.button_recommend)
        layout.addWidget(self.button_play)
        layout.addWidget(self.text_edit)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet('background-color: #00CCCC')

        self.setCentralWidget(widget)

        self.current_song = None

    def recommend_song(self):
        mood = self.input_line_edit.text().lower()
        song_dir = song_directory.get(mood)

        if not song_dir:
            self.text_edit.append(f"Chatbot: Sorry, no songs found for the mood: {mood}")
            self.input_line_edit.clear()
            return

        song_files = os.listdir(song_dir)
        if not song_files:
            self.text_edit.append(f"Chatbot: Sorry, no songs found for the mood: {mood}")
            self.input_line_edit.clear()
            return

        song_file = random.choice(song_files)
        song_path = os.path.join(song_dir, song_file)
        title = os.path.splitext(song_file)[0]

        self.current_song = {"title": title, "file": song_path}

        self.text_edit.append("Chatbot: I recommend the song:")
        self.text_edit.append(f"Title: {title}")
        self.text_edit.append("\n")

        # Display song information
        self.label.setText(f"Now Playing: {title}")

        self.button_play.setEnabled(True)

    def play_song(self):
        if self.current_song:
            song_file = self.current_song["file"]

            pygame.mixer.init()
            pygame.mixer.music.load(song_file)
            pygame.mixer.music.play()

            # Update GUI with song playing status
            self.label.setText(f"Now Playing: {self.current_song['title']} (Playing)")

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

    window = SongRecommender()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
