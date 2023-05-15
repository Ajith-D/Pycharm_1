# 1 Import Libraries
import sys

from PyQt6 import QtWidgets, QtCore, QtGui

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 400
dlg_height = 200

# Title Geometry
title_width = 200
title_height = 20
title_x = int(dlg_width / 2 - dlg_height / 2)
title_y = 20

# Value A Geometry
label1_width = 100
label1_height = 20
label1_x = 50
label1_y = (title_height + title_y) + 20

line1_width = 100
line1_height = 20
line1_x = (label1_x + label1_width) + 20
line1_y = (title_height + title_y) + 20

# Value B Geometry
label2_width = 100
label2_height = 20
label2_x = 50
label2_y = (label1_y + label1_height) + 20

line2_width = 100
line2_height = 20
line2_x = (label2_x + label2_width) + 20
line2_y = (line1_y + line1_height) + 20

# Button Geometry
pushb_width = 100
pushb_height = 30
pushb_x = 50
pushb_y = (label2_y + label2_height) + 20

# Output Geometry
out_width = 100
out_height = 30
out_x = (pushb_x + pushb_width) + 20
out_y = (label2_y + label2_height) + 20

