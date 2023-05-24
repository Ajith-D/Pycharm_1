# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 530
dlg_height = 400

# Title Geometry
title_width = 205
title_height = 20
title_x = 220
title_y = 40

# Label 1 Geometry
lb1_width = 135
lb1_height = 20
lb1_x = 40
lb1_y = 90

# Spin Box 1 Geometry
spin1_width = 40
spin1_height = 20
spin1_x = (lb1_x + lb1_width) + 10
spin1_y = lb1_y - 3

# Label 2 Geometry
lb2_width = 135
lb2_height = 20
lb2_x = 40
lb2_y = (lb1_y + lb1_height) + 10

# Spin Box 2 Geometry
spin2_width = 40
spin2_height = 20
spin2_x = (lb2_x + lb2_width) + 10
spin2_y = lb2_y - 3

# Label 3 Geometry
lb3_width = 135
lb3_height = 20
lb3_x = 40
lb3_y = (lb2_y + lb2_height) + 10

# Spin Box 3 Geometry
spin3_width = 40
spin3_height = 20
spin3_x = (lb3_x + lb3_width) + 10
spin3_y = lb3_y - 3

# Label 4 Geometry
lb4_width = 135
lb4_height = 20
lb4_x = 40
lb4_y = (lb3_y + lb3_height) + 10

# Spin Box 4 Geometry
spin4_width = 40
spin4_height = 20
spin4_x = (lb4_x + lb4_width) + 10
spin4_y = lb4_y - 3

# Label 5 Geometry
lb5_width = 35
lb5_height = 20
lb5_x = (lb1_x + lb1_width) + 40
lb5_y = lb1_y

# Label 6 Geometry
lb6_width = 35
lb6_height = 20
lb6_x = (lb2_x + lb2_width) + 40
lb6_y = lb2_y

# Label 7 Geometry
lb7_width = 35
lb7_height = 20
lb7_x = (lb3_x + lb3_width) + 40
lb7_y = lb3_y

# Label 8 Geometry
lb8_width = 35
lb8_height = 20
lb8_x = (lb4_x + lb4_width) + 40
lb8_y = lb4_y

# PushButton Geometry
pushb_width = 100
pushb_height = 30
pushb_x = spin4_x -50
pushb_y = spin4_y + spin4_height + 30

# Output Geometry
out_width = 220
out_height = 130
out_x = (spin2_x + spin2_width) + 40
out_y = 100

# Label 9 Geometry
lb9_width = 65
lb9_height = 20
lb9_x = title_x + 120
lb9_y = 70

class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('MY SQUAD-2023')
        self.dialog.setStyleSheet('background-color : lightgrey')

        self.title = None
        self.lb1 = None
        self.lb2 = None
        self.lb3 = None
        self.lb4 = None
        self.lb5 = None
        self.lb6 = None
        self.lb7 = None
        self.lb8 = None
        self.lb9 = None
        self.spin1 = None
        self.spin2 = None
        self.spin3 = None
        self.spin4 = None
        self.pushb = None
        self.out = None

    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.lb1 = QLabel(self.dialog)
        self.lb2 = QLabel(self.dialog)
        self.lb3 = QLabel(self.dialog)
        self.lb4 = QLabel(self.dialog)
        self.lb5 = QLabel(self.dialog)
        self.lb6 = QLabel(self.dialog)
        self.lb7 = QLabel(self.dialog)
        self.lb8 = QLabel(self.dialog)
        self.lb9 = QLabel(self.dialog)
        self.spin1 = QSpinBox(self.dialog)
        self.spin2 = QSpinBox(self.dialog)
        self.spin3 = QSpinBox(self.dialog)
        self.spin4 = QSpinBox(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('VGE - SHOPPING')
        self.title.setStyleSheet('color : blue')
        font = QFont('Times')
        font.setBold(True)
        font.setUnderline(True)
        font.setPointSize(11)
        self.title.setFont(font)

        # Label1
        self.lb1.setGeometry(lb1_x, lb1_y, lb1_width, lb1_height)
        self.lb1.setText('Carrot: ')
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb1.setFont(font)

        # SpinBox 1
        self.spin1.setGeometry(spin1_x, spin1_y, spin1_width, spin1_height)
        self.spin1.setMinimum(1)
        self.spin1.setMaximum(60)
        self.spin1.setValue(1)

        # Label2
        self.lb2.setGeometry(lb2_x, lb2_y, lb2_width, lb2_height)
        self.lb2.setText('Onion: ')
        self.lb2.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb2.setFont(font)

        # SpinBox 2
        self.spin2.setGeometry(spin2_x, spin2_y, spin2_width, spin2_height)
        self.spin2.setMinimum(1)
        self.spin2.setMaximum(60)
        self.spin2.setValue(1)

        # Label3
        self.lb3.setGeometry(lb3_x, lb3_y, lb3_width, lb3_height)
        self.lb3.setText('Tomato: ')
        self.lb3.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb3.setFont(font)

        # SpinBox 3
        self.spin3.setGeometry(spin3_x, spin3_y, spin3_width, spin3_height)
        self.spin3.setMinimum(1)
        self.spin3.setMaximum(60)
        self.spin3.setValue(1)

        # Label4
        self.lb4.setGeometry(lb4_x, lb4_y, lb4_width, lb4_height)
        self.lb4.setText('Potato: ')
        self.lb4.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb4.setFont(font)

        # SpinBox 4
        self.spin4.setGeometry(spin4_x, spin4_y, spin4_width, spin4_height)
        self.spin4.setMinimum(1)
        self.spin4.setMaximum(60)
        self.spin4.setValue(1)

        # Label5
        self.lb5.setGeometry(lb5_x, lb5_y, lb5_width, lb5_height)
        self.lb5.setText('KG')
        self.lb5.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb5.setFont(font)

        # Label6
        self.lb6.setGeometry(lb6_x, lb6_y, lb6_width, lb6_height)
        self.lb6.setText('KG')
        self.lb6.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb6.setFont(font)

        # Label7
        self.lb7.setGeometry(lb7_x, lb7_y, lb7_width, lb7_height)
        self.lb7.setText('KG')
        self.lb7.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb7.setFont(font)

        # Label8
        self.lb8.setGeometry(lb8_x, lb8_y, lb8_width, lb8_height)
        self.lb8.setText('KG')
        self.lb8.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb8.setFont(font)

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('ADD KART')
        self.pushb.setStyleSheet('color : white; background-color : black')

        # Output
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.out.setStyleSheet('background-color: lightgrey')
        self.out.setFrameShape(QFrame.Shape.WinPanel)

        # Label9
        self.lb9.setGeometry(lb9_x, lb9_y, lb9_width, lb9_height)
        self.lb9.setText('KART')
        self.lb9.setFrameShape(QFrame.Shape.Panel)
        self.lb9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont('Times')
        font.setBold(True)
        self.lb9.setFont(font)

        # Set Signal and slot
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    def Events(self):
        self.out.setText(f'''1.Carrot {self.spin1.Value()} KG\n\n2.Onion {self.spin2.Value()} KG
        \n3.Tomato{self.spin3.Value()} KG\n\n4.Potato{self.spin4.Value()} KG''')


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
