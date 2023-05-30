# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 500
dlg_height = 400

# Title Geometry
title_width = 150
title_height = 20
title_x = int((dlg_width / 2) - (title_width / 2))
title_y = 20

# Name Geometry
name_width = 100
name_height = 20
name_x = 50
name_y = 70

# Line 1 Geometry
line1_width = 100
line1_height = 20
line1_x = (name_x + name_width) + 10
line1_y = 70

# Age Geometry
age_width = 100
age_height = 20
age_x = 50
age_y = (name_y + name_height) + 10

# Line2 Geometry
line2_width = 30
line2_height = 25
line2_x = (age_x + name_width) + 10
line2_y = line1_y + line1_height + 10