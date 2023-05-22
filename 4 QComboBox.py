# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 500
dlg_height = 650

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
line1_width = 200
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

# Gender Geometry
gen_width = 100
gen_height = 20
gen_x = 50
gen_y = (age_y + age_height) + 10

# ComboBox Geometry
combo_width = 110
combo_height = 35
combo_x = gen_x + gen_width + 5
combo_y = (line2_y + line2_height) + 10

# PushButton Geometry
pushb_width = 100
pushb_height = 30
pushb_x = int((dlg_width / 2) - (pushb_width / 2))
pushb_y = combo_y + combo_height + 20

# Output Geometry
out_width = 400
out_height = 50
out_x = int((dlg_width / 2) - (out_width / 2))
out_y = (pushb_y + pushb_height) + 20





