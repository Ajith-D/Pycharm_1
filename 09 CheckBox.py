# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import pyglet

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 500
dlg_height = 260

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

# Volume Slider Geometry
volume_width = 300
volume_height = 30
volume_x = int((dlg_width / 2) - (volume_width / 2))
volume_y = pushb_y + pushb_height + 40

# Mute CheckBox
mute_width = 100
mute_height = 20
mute_x = 20
mute_y = volume_y + volume_height + 10


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
        self.mute = None
        self.Volume = None
        self.c_volume = None

        # 4 Set Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.song = QLabel(self.dialog)
        self.line1 = QLineEdit(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.Volume = QSlider(self.dialog)
        self.mute = QCheckBox(self.dialog)

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
        self.line1.setText(r"C:\Users\User\Desktop\course\Song\Journey-MassTamilan.fm.mp3")
        self.line1.setStyleSheet('Background-color : lightgrey')

        # For Volume Slider
        self.Volume.setGeometry(volume_x, volume_y, volume_width, volume_height)
        self.Volume.setMinimum(0)
        self.Volume.setMaximum(100)
        self.Volume.setValue(60)
        self.Volume.setOrientation(Qt.Orientation.Horizontal)

        # CheckBox
        self.mute.setGeometry(mute_x, mute_y, mute_width, mute_height)
        self.mute.setText('MUTE')

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('PLAY')
        self.pushb.setStyleSheet('color: white; background-color: black')
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(10)
        self.pushb.setFont(font)

        # Set Signal and slot
        self.pushb.clicked.connect(self.play_song)
        self.Volume.valueChanged.connect(self.update_volume)
        self.mute.stateChanged.connect(self.mute_song)
        QMetaObject.connectSlotsByName(self.dialog)

    # 4 Set Events
    def update_volume(self):
        new = self.Volume.value()
        self.player.volume = new/10

    def play_song(self):
        Song = self.line1.text()
        source = pyglet.media.load(Song, streaming=False)
        self.player = pyglet.media.Player()
        self.player.queue(source)
        self.player.play()

    def mute_song(self):
        if self.player.volume != 0:
            # c_volume - is assumed as constant volume for player.volume
            self.c_volume = self.player.volume

        if self.mute.isChecked():
            self.player.volume = 0
        else:
            self.player.volume = self.c_volume


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
