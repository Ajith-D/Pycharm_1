# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import pyglet

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

# Volume Slider Geometry