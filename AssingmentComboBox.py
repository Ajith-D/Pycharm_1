# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 600
dlg_height = 550

# Title Geometry
title_width = 205
title_height = 20
title_x = 120
title_y = 20

# Label 1 Geometry
lb1_width = 135
lb1_height = 20
lb1_x = 50
lb1_y = 70

# Box 1 Geometry
com1_width = 100
com1_height = 20
com1_x = (lb1_x + lb1_width) + 10
com1_y = 65

# Label 2 Geometry
lb2_width = 135
lb2_height = 20
lb2_x = 50
lb2_y = (lb1_y + lb1_height) + 10

# Box 2 Geometry
com2_width = 100
com2_height = 20
com2_x = (lb2_x + lb2_width) + 10
com2_y = lb2_y - 3

# Label 3 Geometry
lb3_width = 135
lb3_height = 20
lb3_x = 50
lb3_y = (lb2_y + lb2_height) + 10

# Box 3 Geometry
com3_width = 100
com3_height = 20
com3_x = (lb3_x + lb3_width) + 10
com3_y = lb3_y - 3

# Label 4 Geometry
lb4_width = 135
lb4_height = 20
lb4_x = 50
lb4_y = (lb3_y + lb3_height) + 10

# Box 4 Geometry
com4_width = 100
com4_height = 20
com4_x = (lb4_x + lb4_width) + 10
com4_y = lb4_y - 3

# Label 5 Geometry
lb5_width = 135
lb5_height = 20
lb5_x = 50
lb5_y = (lb4_y + lb4_height) + 10

# Box 5 Geometry
com5_width = 100
com5_height = 20
com5_x = (lb5_x + lb5_width) + 10
com5_y = lb5_y - 3

# Label 6 Geometry
lb6_width = 135
lb6_height = 20
lb6_x = 50
lb6_y = (lb5_y + lb5_height) + 10

# Box 6 Geometry
com6_width = 100
com6_height = 20
com6_x = (lb6_x + lb6_width) + 10
com6_y = lb6_y - 3

# Label 7 Geometry
lb7_width = 135
lb7_height = 20
lb7_x = 50
lb7_y = (lb6_y + lb6_height) + 10

# Box 7 Geometry
com7_width = 100
com7_height = 20
com7_x = (lb7_x + lb7_width) + 10
com7_y = lb7_y - 3

# Label 8 Geometry
lb8_width = 135
lb8_height = 20
lb8_x = 50
lb8_y = (lb7_y + lb7_height) + 10


# Box 8 Geometry
com8_width = 100
com8_height = 20
com8_x = (lb8_x + lb8_width) + 10
com8_y = lb8_y - 3

# Label 9 Geometry
lb9_width = 135
lb9_height = 20
lb9_x = 50
lb9_y = (lb8_y + lb8_height) + 10

# Box 9 Geometry
com9_width = 100
com9_height = 20
com9_x = (lb9_x + lb9_width) + 10
com9_y = lb9_y - 3

# Label 10 Geometry
lb10_width = 135
lb10_height = 20
lb10_x = 50
lb10_y = (lb9_y + lb9_height) + 10

# Box 10 Geometry
com10_width = 100
com10_height = 20
com10_x = (lb10_x + lb10_width) + 10
com10_y = lb10_y - 3

# PushButton Geometry
pushb_width = 200
pushb_height = 30
pushb_x = com10_x - 100
pushb_y = com10_y + com10_height + 30

# Output Geometry
out_width = 220
out_height = 320
out_x = (com2_x + com2_width) + 40
out_y = 90

# Label 11 Geometry
lb11_width = 135
lb11_height = 20
lb11_x = (title_x + title_width) + 50
lb11_y = 60


class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('MY SQUAD-2023')
        self.dialog.setStyleSheet('background-color : grey')

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
        self.lb10 = None
        self.lb11 = None
        self.com1 = None
        self.com2 = None
        self.com3 = None
        self.com4 = None
        self.com5 = None
        self.com6 = None
        self.com7 = None
        self.com8 = None
        self.com9 = None
        self.com10 = None
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
        self.lb10 = QLabel(self.dialog)
        self.lb11 = QLabel(self.dialog)
        self.com1 = QComboBox(self.dialog)
        self.com2 = QComboBox(self.dialog)
        self.com3 = QComboBox(self.dialog)
        self.com4 = QComboBox(self.dialog)
        self.com5 = QComboBox(self.dialog)
        self.com6 = QComboBox(self.dialog)
        self.com7 = QComboBox(self.dialog)
        self.com8 = QComboBox(self.dialog)
        self.com9 = QComboBox(self.dialog)
        self.com10 = QComboBox(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('WORLD CUP SQUAD-2023')
        self.title.setStyleSheet('color : #000033')
        font = QFont('Times')
        font.setBold(True)
        font.setUnderline(True)
        font.setPointSize(11)
        self.title.setFont(font)

        # Label1
        self.lb1.setGeometry(lb1_x, lb1_y, lb1_width, lb1_height)
        self.lb1.setText('Top Order Batsman: ')
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb1.setFont(font)

        # Box 1
        self.com1.setGeometry(com1_x, com1_y, com1_width, com1_height)
        self.com1.setStyleSheet('Background-color : lightgrey')
        self.com1.addItem('Rohit Sharma')
        self.com1.addItem('Subham Gill')
        self.com1.addItem('Virat Kholi')
        self.com1.addItem('Sanju Samson')
        self.com1.addItem('Jadeja')
        self.com1.addItem('Hardik Pandya')
        self.com1.addItem('Axar Patel')
        self.com1.addItem('Siraj')
        self.com1.addItem('Bumrah')
        self.com1.addItem('Shami')

        # Label2
        self.lb2.setGeometry(lb2_x, lb2_y, lb2_width, lb2_height)
        self.lb2.setText('Top Order Batsman: ')
        self.lb2.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb2.setFont(font)

        # Box2
        self.com2.setGeometry(com2_x, com2_y, com2_width, com2_height)
        self.com2.setStyleSheet('Background-color : lightgrey')
        self.com2.addItem('Rohit Sharma')
        self.com2.addItem('Subham Gill')
        self.com2.addItem('Virat Kholi')
        self.com2.addItem('Sanju Samson')
        self.com2.addItem('Jadeja')
        self.com2.addItem('Hardik Pandya')
        self.com2.addItem('Axar Patel')
        self.com2.addItem('Siraj')
        self.com2.addItem('Bumrah')
        self.com2.addItem('Shami')

        # Label3
        self.lb3.setGeometry(lb3_x, lb3_y, lb3_width, lb3_height)
        self.lb3.setText('Top Order Batsman: ')
        self.lb3.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb3.setFont(font)

        # Box3
        self.com3.setGeometry(com3_x, com3_y, com3_width, com3_height)
        self.com3.setStyleSheet('Background-color : lightgrey')
        self.com3.addItem('Rohit Sharma')
        self.com3.addItem('Subham Gill')
        self.com3.addItem('Virat Kholi')
        self.com3.addItem('Sanju Samson')
        self.com3.addItem('Jadeja')
        self.com3.addItem('Hardik Pandya')
        self.com3.addItem('Axar Patel')
        self.com3.addItem('Siraj')
        self.com3.addItem('Bumrah')
        self.com3.addItem('Shami')

        # Label4
        self.lb4.setGeometry(lb4_x, lb4_y, lb4_width, lb4_height)
        self.lb4.setText('Middle Order Batsman: ')
        self.lb4.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb4.setFont(font)

        # Box4
        self.com4.setGeometry(com4_x, com4_y, com4_width, com4_height)
        self.com4.setStyleSheet('Background-color : lightgrey')
        self.com4.addItem('Rohit Sharma')
        self.com4.addItem('Subham Gill')
        self.com4.addItem('Virat Kholi')
        self.com4.addItem('Sanju Samson')
        self.com4.addItem('Jadeja')
        self.com4.addItem('Hardik Pandya')
        self.com4.addItem('Axar Patel')
        self.com4.addItem('Siraj')
        self.com4.addItem('Bumrah')
        self.com4.addItem('Shami')

        # Label5
        self.lb5.setGeometry(lb5_x, lb5_y, lb5_width, lb5_height)
        self.lb5.setText('All Rounder: ')
        self.lb5.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb5.setFont(font)

        # Box5
        self.com5.setGeometry(com5_x, com5_y, com5_width, com5_height)
        self.com5.setStyleSheet('Background-color : lightgrey')
        self.com5.addItem('Rohit Sharma')
        self.com5.addItem('Subham Gill')
        self.com5.addItem('Virat Kholi')
        self.com5.addItem('Sanju Samson')
        self.com5.addItem('Jadeja')
        self.com5.addItem('Hardik Pandya')
        self.com5.addItem('Axar Patel')
        self.com5.addItem('Siraj')
        self.com5.addItem('Bumrah')
        self.com5.addItem('Shami')

        # Label6
        self.lb6.setGeometry(lb6_x, lb6_y, lb6_width, lb6_height)
        self.lb6.setText('All Rounder: ')
        self.lb6.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb6.setFont(font)

        # Box6
        self.com6.setGeometry(com6_x, com6_y, com6_width, com6_height)
        self.com6.setStyleSheet('Background-color : lightgrey')
        self.com6.addItem('Rohit Sharma')
        self.com6.addItem('Subham Gill')
        self.com6.addItem('Virat Kholi')
        self.com6.addItem('Sanju Samson')
        self.com6.addItem('Jadeja')
        self.com6.addItem('Hardik Pandya')
        self.com6.addItem('Axar Patel')
        self.com6.addItem('Siraj')
        self.com6.addItem('Bumrah')
        self.com6.addItem('Shami')

        # Label7
        self.lb7.setGeometry(lb7_x, lb7_y, lb7_width, lb7_height)
        self.lb7.setText('All Rounder: ')
        self.lb7.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb7.setFont(font)

        # Box7
        self.com7.setGeometry(com7_x, com7_y, com7_width, com7_height)
        self.com7.setStyleSheet('Background-color : lightgrey')
        self.com7.addItem('Rohit Sharma')
        self.com7.addItem('Subham Gill')
        self.com7.addItem('Virat Kholi')
        self.com7.addItem('Sanju Samson')
        self.com7.addItem('Jadeja')
        self.com7.addItem('Hardik Pandya')
        self.com7.addItem('Axar Patel')
        self.com7.addItem('Siraj')
        self.com7.addItem('Bumrah')
        self.com7.addItem('Shami')

        # Label8
        self.lb8.setGeometry(lb8_x, lb8_y, lb8_width, lb8_height)
        self.lb8.setText('BOWLER: ')
        self.lb8.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb8.setFont(font)

        # Box8
        self.com8.setGeometry(com8_x, com8_y, com8_width, com8_height)
        self.com8.setStyleSheet('Background-color : lightgrey')
        self.com8.addItem('Rohit Sharma')
        self.com8.addItem('Subham Gill')
        self.com8.addItem('Virat Kholi')
        self.com8.addItem('Sanju Samson')
        self.com8.addItem('Jadeja')
        self.com8.addItem('Hardik Pandya')
        self.com8.addItem('Axar Patel')
        self.com8.addItem('Siraj')
        self.com8.addItem('Bumrah')
        self.com8.addItem('Shami')

        # Label9
        self.lb9.setGeometry(lb9_x, lb9_y, lb9_width, lb9_height)
        self.lb9.setText('BOWLER: ')
        self.lb9.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb9.setFont(font)

        # Box9
        self.com9.setGeometry(com9_x, com9_y, com9_width, com9_height)
        self.com9.setStyleSheet('Background-color : lightgrey')
        self.com9.addItem('Rohit Sharma')
        self.com9.addItem('Subham Gill')
        self.com9.addItem('Virat Kholi')
        self.com9.addItem('Sanju Samson')
        self.com9.addItem('Jadeja')
        self.com9.addItem('Hardik Pandya')
        self.com9.addItem('Axar Patel')
        self.com9.addItem('Siraj')
        self.com9.addItem('Bumrah')
        self.com9.addItem('Shami')

        # Label10
        self.lb10.setGeometry(lb10_x, lb10_y, lb10_width, lb10_height)
        self.lb10.setText('BOWLER: ')
        self.lb10.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb10.setFont(font)

        # Box10
        self.com10.setGeometry(com10_x, com10_y, com10_width, com10_height)
        self.com10.setStyleSheet('Background-color : lightgrey')
        self.com10.addItem('Rohit Sharma')
        self.com10.addItem('Subham Gill')
        self.com10.addItem('Virat Kholi')
        self.com10.addItem('Sanju Samson')
        self.com10.addItem('Jadeja')
        self.com10.addItem('Hardik Pandya')
        self.com10.addItem('Axar Patel')
        self.com10.addItem('Siraj')
        self.com10.addItem('Bumrah')
        self.com10.addItem('Shami')

        # Label11
        self.lb11.setGeometry(lb11_x, lb11_y, lb11_width, lb11_height)
        self.lb11.setText('SELECTED TEAM')
        self.lb11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb11.setStyleSheet('color : #000033')
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(10)
        self.lb11.setFont(font)

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('ADD PLAYER')
        self.pushb.setStyleSheet('color : white; background-color : black')
        font = QFont('Times')
        font.setBold(True)
        self.pushb.setFont(font)

        # Output
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.out.setStyleSheet('background-color: lightgrey')
        self.out.setFrameShape(QFrame.Shape.WinPanel)

        # Set Signal and slot
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    def Events(self):
        self.out.setText(f'''1.{self.com1.currentText()}-Top Order Batsmen\n\n2.{self.com2.currentText()}-Top Order Batsmen
    \n3.{self.com3.currentText()}-Top Order Batsmen\n\n4.{self.com4.currentText()}-Middle Order Batsmen
    \n5.{self.com5.currentText()}-All rounder\n\n6.{self.com6.currentText()}All rounder\n\n7.{self.com7.currentText()}-All rounder
    \n8.{self.com8.currentText()}-Bowler\n\n9.{self.com9.currentText()}-Bowler\n\n10.{self.com10.currentText()}-Bowler''')

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
