# 1 Import Libraries
import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 400
dlg_height = 200

# Title Geometry
title_width = 200
title_height = 20
title_x = int(dlg_width / 2 - title_width/ 2)
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

# 3 Create Class
class AppForm:
    def __init__(self, form):
        # form = QtWidgets.QWidget()
        self.dialog = form
        self.dialog.setObjectName("My App")
        self.dialog.setEnabled(True)
        self.dialog.setGeometry(100, 200, dlg_width, dlg_height)
        self.dialog.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.dialog.setWindowTitle("My Window")
        self.dialog.setWindowOpacity(1.0)

        # Define Fields
        self.title = None
        self.label1 = None
        self.label2 = None
        self.line1 = None
        self.line2 = None
        self.pushb = None
        self.out = None


    # 4 Create Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.label1 = QLabel(self.dialog)
        self.label2 = QLabel(self.dialog)
        self.line1 = QLineEdit(self.dialog)
        self.line2 = QLineEdit(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # For Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('ADDITION')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # For Label 1
        self.label1.setGeometry(label1_x, label1_y, label1_width, label1_height)
        self.label1.setText('Value A: ')

        # For Line 1
        self.line1.setGeometry(line1_x, line1_y, line1_width, line1_height)

        # For Label 2
        self.label2.setGeometry(label2_x, label2_y, label2_width, label2_height)
        self.label2.setText('Value B: ')

        # For Line 2
        self.line2.setGeometry(line2_x, line2_y, line2_width, line2_height)

        # Set PushButton
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('ADD')

        # Set OutPut
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setText('ANS: ')

        # Set Signal
        self.pushb.clicked.connect(self.Event)
        # set Slot
        QMetaObject.connectSlotsByName(self.dialog)

    def Event(self):
        x = self.line1.text()
        y = self.line2.text()
        add = float(x) + float(y)
        self.out.setText(f'Ans: {str(add)}')

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