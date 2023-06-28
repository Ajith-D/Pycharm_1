import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMessageBox, QLineEdit, QSlider
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import random
import pygame
import os
import cv2
from deepface import DeepFace

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

        self.button_play = QPushButton("Play")
        self.button_play.setEnabled(False)
        self.button_play.clicked.connect(self.play_pause_song)
        self.button_play.setStyleSheet('color: white; background-color: black')

        self.button_next = QPushButton("Next")
        self.button_next.setEnabled(False)
        self.button_next.clicked.connect(self.next_song)
        self.button_next.setStyleSheet('color: white; background-color: black')

        self.slider_volume = QSlider(Qt.Orientation.Horizontal)
        self.slider_volume.setMinimum(0)
        self.slider_volume.setMaximum(100)
        self.slider_volume.setValue(80)
        self.slider_volume.setTickInterval(10)
        self.slider_volume.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_volume.valueChanged.connect(self.set_volume)

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
        layout.addWidget(self.button_next)
        layout.addWidget(self.slider_volume)
        layout.addWidget(self.text_edit)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet('background-color: #00CCCC')

        self.setCentralWidget(widget)

        self.current_song = None
        self.is_playing = False

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

        # Perform face emotion recognition using the camera
        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            if not ret:
                break

            # Perform emotion recognition on the captured frame
            result = DeepFace.analyze(frame, actions=["emotion"])
            emotion = result["dominant_emotion"]

            # Check if the recognized emotion matches the recommended mood
            if emotion.lower() == mood:
                break

            cv2.imshow("Emotion Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        capture.release()
        cv2.destroyAllWindows()

        self.button_play.setEnabled(True)
        self.button_next.setEnabled(True)

    def play_pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        if self.current_song:
            if not self.is_playing:
                # Play song
                song_file = self.current_song["file"]
                pygame.mixer.init()
                pygame.mixer.music.load(song_file)
                pygame.mixer.music.play()
                self.is_playing = True
                self.button_play.setText("Pause")
            else:
                # Pause song
                pygame.mixer.music.pause()
                self.is_playing = False
                self.button_play.setText("Play")

            pygame.mixer.init()

    def next_song(self):
        self.play_pause_song()  # Pause current song before selecting next song

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

        song_files.remove(os.path.basename(self.current_song["file"]))  # Remove current song from list

        if len(song_files) == 0:
            self.text_edit.append("Chatbot: No more songs found for the given mood.")
            self.input_line_edit.clear()
            return

        song_file = random.choice(song_files)
        song_path = os.path.join(song_dir, song_file)
        title = os.path.splitext(song_file)[0]

        self.current_song = {"title": title, "file": song_path}

        self.text_edit.append("Chatbot: I recommend the next song:")
        self.text_edit.append(f"Title: {title}")
        self.text_edit.append("\n")

        # Display song information
        self.label.setText(f"Now Playing: {title}")

        self.play_pause_song()  # Resume playing the next song

    def set_volume(self, value):
        volume = value / 100.0
        pygame.mixer.music.set_volume(volume)

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
