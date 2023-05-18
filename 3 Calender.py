# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 400
dlg_height = 280

# Title Geometry
title_width = 200
title_height = 20
title_x = int((dlg_width / 2) - (title_width / 2))
title_y = 20

# Task Geometry
task_width = 100
task_height = 20
task_x = 10
task_y = title_y + 20

line_width = 300
line_height = 25
line_x = (task_x + task_width) + 10
line_y = task_y - 3

# Calendar Geometry
cal_width = 300
cal_height = 300
cal_x = int((dlg_width / 2) - (cal_width / 2))
cal_y = line_y + 50

# Button Geometry
pushb_width = 150
pushb_height = 50
pushb_x = int((dlg_width / 2) - (pushb_width / 2))
pushb_y = (cal_y + cal_height) + 50

# Output Geometry
out_width = 400
out_height = 50
out_x = 50
out_y = (pushb_y + pushb_height) + 20

# 3 Create Class
class AppForm:
    def __init__(self, form):
        form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Task Manager')





