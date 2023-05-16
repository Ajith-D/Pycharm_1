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
title_x = int(dlg_width / 2 - title_width / 2)
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
pushb1_width = 80
pushb1_height = 20
pushb1_x = 40
pushb1_y = (label2_y + label2_height) + 20

pushb2_width = 80
pushb2_height = 20
pushb2_x = 160
pushb2_y = (label1_y + label1_height) + 60

pushb3_width = 80
pushb3_height = 20
pushb3_x = 40
pushb3_y = (label2_y + label2_height) + 60

pushb4_width = 80
pushb4_height = 20
pushb4_x = 160
pushb4_y = (label1_y + label1_height) + 100

pushb5_width = 80
pushb5_height = 20
pushb5_x = 40
pushb5_y = (label2_y + label2_height) + 100

pushb6_width = 80
pushb6_height = 20
pushb6_x = 160
pushb6_y = (label1_y + label1_height) + 140

# Output Geometry
out_width = 100
out_height = 20
out_x = (pushb1_x + pushb1_width) + 170
out_y = (label2_y + label2_height) + 20

# 3 Create Class
class AppForm:
    def __init__(self, form):
        # form = QtWidgets.QWidget()
        self.dialog = form
        self.dialog.setObjectName("My App")
        self.dialog.setEnabled(True)
        self.dialog.setGeometry(130, 270, dlg_width, dlg_height)
        self.dialog.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.dialog.setWindowTitle("My Window")
        self.dialog.setWindowOpacity(1.0)

        # Define Fields
        self.title = None
        self.label1 = None
        self.label2 = None
        self.line1 = None
        self.line2 = None
        self.pushb1 = None
        self.pushb2 = None
        self.pushb3 = None
        self.pushb4 = None
        self.pushb5 = None
        self.pushb6 = None
        self.out = None

    # 4 Create Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.label1 = QLabel(self.dialog)
        self.label2 = QLabel(self.dialog)
        self.line1 = QLineEdit(self.dialog)
        self.line2 = QLineEdit(self.dialog)
        self.pushb1 = QPushButton(self.dialog)
        self.pushb2 = QPushButton(self.dialog)
        self.pushb3 = QPushButton(self.dialog)
        self.pushb4 = QPushButton(self.dialog)
        self.pushb5 = QPushButton(self.dialog)
        self.pushb6 = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # For Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('CALCULATOR')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont('Times')
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)

        # For Label 1
        self.label1.setGeometry(label1_x, label1_y, label1_width, label1_height)
        self.label1.setText('VALUE A: ')
        font = QFont('Times')
        font.setBold(True)
        self.label1.setFont(font)

        # For Line 1
        self.line1.setGeometry(line1_x, line1_y, line1_width, line1_height)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # For Label 2
        self.label2.setGeometry(label2_x, label2_y, label2_width, label2_height)
        self.label2.setText('VALUE B: ')
        font = QFont('Times')
        font.setBold(True)
        self.label2.setFont(font)

        # For Line 2
        self.line2.setGeometry(line2_x, line2_y, line2_width, line2_height)
        self.line2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set PushButton 1
        self.pushb1.setGeometry(pushb1_x, pushb1_y, pushb1_width, pushb1_height)
        self.pushb1.setText('ADD')
        self.pushb1.setStyleSheet("color: white; background-color: Black")

        # Set PushButton 2
        self.pushb2.setGeometry(pushb2_x, pushb2_y, pushb2_width, pushb2_height)
        self.pushb2.setText('SUB')
        self.pushb2.setStyleSheet("color: white; background-color: Black")

        # Set PushButton 3
        self.pushb3.setGeometry(pushb3_x, pushb3_y, pushb3_width, pushb3_height)
        self.pushb3.setText('MULTIPLY')
        self.pushb3.setStyleSheet("color: white; background-color: Black")

        # Set PushButton 4
        self.pushb4.setGeometry(pushb4_x, pushb4_y, pushb4_width, pushb4_height)
        self.pushb4.setText('DIVIDE')
        self.pushb4.setStyleSheet("color: white; background-color: Black")

        # Set PushButton 5
        self.pushb5.setGeometry(pushb5_x, pushb5_y, pushb5_width, pushb5_height)
        self.pushb5.setText('REMAINDER')
        self.pushb5.setStyleSheet("color: white; background-color: Black")

        # Set PushButton 6
        self.pushb6.setGeometry(pushb6_x, pushb6_y, pushb6_width, pushb6_height)
        self.pushb6.setText('QUOTIENT')
        self.pushb6.setStyleSheet("color: white; background-color: Black")

        # Set OutPut
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setText('ANS: ')
        self.out.setFrameShape(QFrame.Shape.Box)
        self.out.setStyleSheet("background-color: lightGrey")


        # Set Signal
        self.pushb1.clicked.connect(self.Event1)
        self.pushb2.clicked.connect(self.Event2)
        self.pushb3.clicked.connect(self.Event3)
        self.pushb4.clicked.connect(self.Event4)
        self.pushb5.clicked.connect(self.Event5)
        self.pushb6.clicked.connect(self.Event6)
        # set Slot
        QMetaObject.connectSlotsByName(self.dialog)

    def Event1(self):
        x = self.line1.text()
        y = self.line2.text()
        add = float(x) + float(y)
        self.out.setText(f'ANS: {str(add)}')

    def Event2(self):
        x = self.line1.text()
        y = self.line2.text()
        sub = float(x) - float(y)
        self.out.setText(f'ANS: {str(sub)}')
    def Event3(self):
        x = self.line1.text()
        y = self.line2.text()
        multiply = float(x) * float(y)
        self.out.setText(f'ANS: {str(multiply)}')
    def Event4(self):
        x = self.line1.text()
        y = self.line2.text()
        divide = float(x) / float(y)
        self.out.setText(f'ANS: {str(divide)}')
    def Event5(self):
        x = self.line1.text()
        y = self.line2.text()
        rem = float(x) % float(y)
        self.out.setText(f'ANS: {str(rem)}')
    def Event6(self):
        x = self.line1.text()
        y = self.line2.text()
        quo = float(x) // float(y)
        self.out.setText(f'ANS: {str(quo)}')


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
