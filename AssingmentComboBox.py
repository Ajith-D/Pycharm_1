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
line6_y = lb6_y - 3

# Label 7 Geometry
lb7_width = 135
lb7_height = 20
lb7_x = 50
lb7_y = (lb6_y + lb6_height) + 10

# Line 7 Geometry
line7_width = 100
line7_height = 20
line7_x = (lb7_x + lb7_width) + 10
line7_y = lb7_y - 3

# Label 8 Geometry
lb8_width = 135
lb8_height = 20
lb8_x = 50
lb8_y = (lb7_y + lb7_height) + 10

# Line 8 Geometry
line8_width = 100
line8_height = 20
line8_x = (lb8_x + lb8_width) + 10
line8_y = lb8_y - 3

# Label 9 Geometry
lb9_width = 135
lb9_height = 20
lb9_x = 50
lb9_y = (lb8_y + lb8_height) + 10

# Line 9 Geometry
line9_width = 100
line9_height = 20
line9_x = (lb9_x + lb9_width) + 10
line9_y = lb9_y - 3

# Label 10 Geometry
lb10_width = 135
lb10_height = 20
lb10_x = 50
lb10_y = (lb9_y + lb9_height) + 10

# Line 10 Geometry
line10_width = 100
line10_height = 20
line10_x = (lb10_x + lb10_width) + 10
line10_y = lb10_y - 3

class AppForm:
    def __init__(self, form):
        # form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('MY SQUAD-2023')

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
        self.line1 = None
        self.line2 = None
        self.line3 = None
        self.line4 = None
        self.line5 = None
        self.line6 = None
        self.line7 = None
        self.line8 = None
        self.line9 = None
        self.line10 = None

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
        self.line1 = QLineEdit(self.dialog)
        self.line2 = QLineEdit(self.dialog)
        self.line3 = QLineEdit(self.dialog)
        self.line4 = QLineEdit(self.dialog)
        self.line5 = QLineEdit(self.dialog)
        self.line6 = QLineEdit(self.dialog)
        self.line7 = QLineEdit(self.dialog)
        self.line8 = QLineEdit(self.dialog)
        self.line9 = QLineEdit(self.dialog)
        self.line10 = QLineEdit(self.dialog)


        # Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('WORLD CUP SQUAD-2023')
        self.title.setStyleSheet('color : blue')
        font = QFont('Times')
        font.setBold(True)
        font.setUnderline(True)
        font.setPointSize(12)
        self.title.setFont(font)

        # Label1
        self.lb1.setGeometry(lb1_x, lb1_y, lb1_width, lb1_height)
        self.lb1.setText('Top Order Batsman: ')
        self.lb1.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb1.setFont(font)

        # Line1
        self.line1.setGeometry(line1_x, line1_y, line1_width, line1_height)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line1.setStyleSheet('Background-color : lightgrey')

        # Label2
        self.lb2.setGeometry(lb2_x, lb2_y, lb2_width, lb2_height)
        self.lb2.setText('Top Order Batsman: ')
        self.lb2.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb2.setFont(font)

        # Line2
        self.line2.setGeometry(line2_x, line2_y, line2_width, line2_height)
        self.line2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line2.setStyleSheet('Background-color : lightgrey')

        # Label3
        self.lb3.setGeometry(lb3_x, lb3_y, lb3_width, lb3_height)
        self.lb3.setText('Top Order Batsman: ')
        self.lb3.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb3.setFont(font)

        # Line3
        self.line3.setGeometry(line3_x, line3_y, line3_width, line3_height)
        self.line3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line3.setStyleSheet('Background-color : lightgrey')

        # Label4
        self.lb4.setGeometry(lb4_x, lb4_y, lb4_width, lb4_height)
        self.lb4.setText('Middle Order Batsman: ')
        self.lb4.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb4.setFont(font)

        # Line4
        self.line4.setGeometry(line4_x, line4_y, line4_width, line4_height)
        self.line4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line4.setStyleSheet('Background-color : lightgrey')

        # Label5
        self.lb5.setGeometry(lb5_x, lb5_y, lb5_width, lb5_height)
        self.lb5.setText('All Rounder: ')
        self.lb5.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb5.setFont(font)

        # Line5
        self.line5.setGeometry(line5_x, line5_y, line5_width, line5_height)
        self.line5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line5.setStyleSheet('Background-color : lightgrey')

        # Label6
        self.lb6.setGeometry(lb6_x, lb6_y, lb6_width, lb6_height)
        self.lb6.setText('All Rounder: ')
        self.lb6.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb6.setFont(font)

        # Line6
        self.line6.setGeometry(line6_x, line6_y, line6_width, line6_height)
        self.line6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line6.setStyleSheet('Background-color : lightgrey')

        # Label7
        self.lb7.setGeometry(lb7_x, lb7_y, lb7_width, lb7_height)
        self.lb7.setText('All Rounder: ')
        self.lb7.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb7.setFont(font)

        # Line7
        self.line7.setGeometry(line7_x, line7_y, line7_width, line7_height)
        self.line7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line7.setStyleSheet('Background-color : lightgrey')

        # Label8
        self.lb8.setGeometry(lb8_x, lb8_y, lb8_width, lb8_height)
        self.lb8.setText('BOWLER: ')
        self.lb8.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb8.setFont(font)

        # Line8
        self.line8.setGeometry(line8_x, line8_y, line8_width, line8_height)
        self.line8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line8.setStyleSheet('Background-color : lightgrey')

        # Label9
        self.lb9.setGeometry(lb9_x, lb9_y, lb9_width, lb9_height)
        self.lb9.setText('BOWLER: ')
        self.lb9.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb9.setFont(font)

        # Line9
        self.line9.setGeometry(line9_x, line9_y, line9_width, line9_height)
        self.line9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line9.setStyleSheet('Background-color : lightgrey')

        # Label10
        self.lb10.setGeometry(lb10_x, lb10_y, lb10_width, lb10_height)
        self.lb10.setText('BOWLER: ')
        self.lb10.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        self.lb10.setFont(font)

        # Line10
        self.line10.setGeometry(line10_x, line10_y, line10_width, line10_height)
        self.line10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line10.setStyleSheet('Background-color : lightgrey')


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
