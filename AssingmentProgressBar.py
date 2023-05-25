# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import os
import fnmatch

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 500
dlg_height = 500

# Title Geometry
title_width = 150
title_height = 20
title_x = int((dlg_width / 2) - (title_width / 2))
title_y = 20

# Path Geometry
path_width = 70
path_height = 20
path_x = 50
path_y = 70

# Line 1 Geometry
line1_width = 300
line1_height = 20
line1_x = path_x + 60
line1_y = path_y + 30

# Label 2 Geometry
label2_width = 100
label2_height = 20
label2_x = line1_x + 60
label2_y = line1_y + 60

# Output Geometry
out_width = 70
out_height = 25
out_x = label2_x + 100
out_y = label2_y - 2

# pushb Geometry
pushb_width = 190
pushb_height = 30
pushb_x = line1_x + 50
pushb_y = (out_y + out_width) - 5

# Progress Bar Geometry
bar_width = dlg_width - 80
bar_height = 20
bar_x = 40
bar_y = out_y + pushb_y + 20

# 3 Style Sheet For Progress Bar
progress_style = '''
QProgressBar {
     border: 2px solid  grey;
     border-radius: 5px;
     background-color: #FFFFCC;
     height: 5;
}

QProgressBar::chunk {
     background-color: #556B2F;
     width: 10px;
}
'''

# 4 Create Class
class AppForm:
    def __init__(self, form):
        # form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('INDO VIRUS')
        self.dialog.setStyleSheet('background-color: #00CCCC')

        self.title = None
        self.Path = None
        self.line1 = None
        self.bar = None
        self.label2 = None
        self.pushb = None
        self.out = None

    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.Path = QLabel(self.dialog)
        self.line1 = QLineEdit(self.dialog)
        self.bar = QProgressBar(self.dialog)
        self.label2 = QLabel(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # Title
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        self.title.setText('INDO VIRUS')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(15)
        self.title.setFont(font)

        # PATH
        self.Path.setGeometry(path_x, path_y, path_width, path_height)
        self.Path.setText('PATH: ')
        self.Path.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(10)
        self.Path.setFont(font)

        # Line1
        self.line1.setGeometry(line1_x, line1_y, line1_width, line1_height)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.line1.setText(r'')
        self.line1.setStyleSheet('Background-color : lightgrey')

        # Progress Bar
        self.bar.setGeometry(bar_x, bar_y, bar_width, bar_height)
        self.bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bar.setStyleSheet(progress_style)
        self.bar.setStyleSheet("QProgressBar")

        # For Label 2
        self.label2.setGeometry(label2_x, label2_y, label2_width, label2_height)
        self.label2.setText('FILE QUANTITY: ')
        font = QFont('Times')
        font.setBold(True)
        self.label2.setFont(font)

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('ANALYZE')
        self.pushb.setStyleSheet('color: white; background-color: black')

        # Output
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.out.setFrameShape(QFrame.Shape.WinPanel)
        self.out.setStyleSheet('color: black; background-color: lightgrey')
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(10)
        self.out.setFont(font)

        # Set Signal and slot
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    def Events(self):
        output = '\n'
        root = self.line1.text()

        # Like While & for Statement
        total_files = 0
        for path, subdir, files, in os.walk(root):
            count = len(fnmatch.filter(os.listdir(path), '*.*'))
            total_files = total_files + count

        self.out.setText(f'{total_files}')

        #Set Progress Minimum & Maximum
        self.bar.setMinimum(0)
        self.bar.setMaximum(total_files)

        count = 0
        for path, subdir, files, in os.walk(root):
            for file in files:
                count = count + 1
                self.bar.setValue(count)
                output = file + '\n' + output
                QApplication.processEvents()



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