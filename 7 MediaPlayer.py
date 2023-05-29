# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 500
dlg_height = 230

# Title Geometry
title_width = 200
title_height = 40
title_x = int((dlg_width / 2) - (title_width / 2))
title_y = 20

# Mp_3 Path Geometry
song_width = 80
song_height = 30
song_x = 0
song_y = (title_height + title_y) + 20

line1_width = 300
line1_height = 25
line1_x = (song_x + song_width) + 10
line1_y = song_y - 5

# Button Geometry
pushb_width = 70
pushb_height = 25
pushb_x = (line1_x + line1_width) + 10
pushb_y = song_y - 4


# 3 Create Class
class AppForm:
    def __init__(self, form):
        # form = QtWidgets.QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 200, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Media Player')
        self.dialog.setStyleSheet('background-color: #FFEFD5')

        self.title = None
        self.song = None
        self.pushb = None
        self.line1 = None
        self.player = None
        self.audio = None

    # 4 Set Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.song = QLabel(self.dialog)
        self.line1 = QLineEdit(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.player = QMediaPlayer(self.dialog)
        self.audio = QAudioOutput(self.dialog)

        # For Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('MUSIC PLAYER')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont('Times')
        font.setBold(True)
        font.setUnderline(True)
        font.setPointSize(15)
        self.title.setFont(font)

        # For Song
        self.song.setGeometry(song_x, song_y, song_width, song_height)
        self.song.setText('SONG: ')
        self.song.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(10)
        self.song.setFont(font)

        # Line1
        self.line1.setGeometry(line1_x, line1_y, line1_width, line1_height)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.line1.setText("C:\Users\User\Desktop\course\Song\journey.mp3")
        self.line1.setStyleSheet('Background-color : lightgrey')

        # For Player & Audio
        #self.audio.setVolume(70)
        #self.player.setAudioOutput(self.audio)

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('PLAY')
        self.pushb.setStyleSheet('color: white; background-color: black')
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(10)
        self.pushb.setFont(font)

        # Set Signal and slot
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    # 4 Set Event
    def Events(self):
        Song = self.line1.currentText()
        url = QUrl.fromLocalFile(Song)
        self.player.setSource(url)
        self.player.play()


# 5 Execute Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()

    # Give the form class
    userI = AppForm(Form)

    # Initialize the Widget
    userI.Widgets()

    # Show Form
    Form.show()

    # Close the Form
    sys.exit(app.exec())
