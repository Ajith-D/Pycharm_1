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

# Gender Geometry
gen_width = 100
gen_height = 20
gen_x = 50
gen_y = (age_y + age_height) + 20

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

class AppForm:
    def __init__(self, form):
        # form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Sign-up Form')

        self.title = None
        self.name = None
        self.line1 = None
        self.age = None
        self.line2 = None
        self.gen = None
        self.com = None
        self.pushb = None
        self.out = None

    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.name = QLabel(self.dialog)
        self.line1 = QLineEdit(self.dialog)
        self.age = QLabel(self.dialog)
        self.line2 = QLineEdit(self.dialog)
        self.gen = QLabel(self.dialog)
        self.com = QComboBox(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('AATOMZ')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Name
        self.name.setGeometry(name_x, name_y, name_width, name_height)
        self.name.setText('NAME: ')
        self.name.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Line1
        self.line1.setGeometry(line1_x, line1_y, line1_width, line1_height)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line1.setStyleSheet('Background-color : lightgrey')

        # Age
        self.age.setText('AGE: ')
        self.age.setGeometry(age_x, age_y, age_width, age_height)
        self.age.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Line 2
        self.line2.setGeometry(line2_x, line2_y, line2_width, line2_height)
        self.line2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line2.setStyleSheet('Background-color : lightgrey')

        # Gender
        self.gen.setGeometry(gen_x, gen_y, gen_width, gen_height)
        self.gen.setText('GENDER: ')
        self.gen.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Combo Box
        self.com.setGeometry(combo_x, combo_y, combo_width, combo_height)
        self.com.setObjectName('COMBO BOX')
        self.com.addItem('MALE')
        self.com.addItem('FEMALE')

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('SIGN UP')

        # Output
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set Signal and slot
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    def Events(self):
        if self.com.currentText() == 'MALE':
            self.out.setText(f'''Welcome Sir!\n{self.line1.text()}
        Successfully Signed Up''')

        else:
            self.out.setText(f'''Welcome Madam!\n{self.line1.text()}
        Successfully Signed Up''')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()

    # Give the Form class
    user = AppForm(Form)

    # Initialize the Widget
    user.Widgets()

    # Form Show
    Form.show()

    # Close
    sys.exit(app.exec())
