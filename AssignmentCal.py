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
title_width = 200
title_height = 20
title_x = int((dlg_width / 2) - (title_width / 2)) + 40
title_y = 20

# Task Geometry
task_width = 100
task_height = 20
task_x = 80
task_y = title_y + 40

line_width = 130
line_height = 25
line_x = (task_x + task_width) + 10
line_y = task_y - 3

# Calendar Geometry
cal_width = 400
cal_height = 300
cal_x = int((dlg_width / 2) - (cal_width / 2))
cal_y = line_y + 50

# Button Geometry
pushb_width = 180
pushb_height = 40
pushb_x = int((dlg_width / 2) - (pushb_width / 2))
pushb_y = (cal_y + cal_height) + 10

# Output Geometry
out_width = 400
out_height = 100
out_x = 50
out_y = (pushb_y + pushb_height) + 20

Tasks = ''

# 3 Create Class
class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setWindowTitle('My Claculator')
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setStyleSheet('background-color : lightgrey')

        # Define Fields
        self.out = None
        self.pushb = None
        self.cal = None
        self.line = None
        self.task = None
        self.title = None

    # 4 Set Widgets
    def Widgets(self):

        self.title = QLabel(self.dialog)
        self.task = QLabel(self.dialog)
        self.line = QLineEdit(self.dialog)
        self.cal = QCalendarWidget(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # Title
        self.title.setText('Task Manager')
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        font = QFont('Times')
        font.setBold(True)
        font.setUnderline(True)
        font.setPointSize(16)
        self.title.setFont(font)

        # Task
        self.task.setGeometry(task_x, task_y, task_width, task_height)
        self.task.setText('Task: ')
        self.task.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Line
        self.line.setGeometry(line_x, line_y, line_width, line_height)
        self.line.setStyleSheet('Background-color : white')

        # Calender
        self.cal.setGeometry(cal_x, cal_y, cal_width, cal_height)
        self.cal.setGridVisible(True)
        self.cal.setMinimumDate(QDate.currentDate())
        self.cal.setStyleSheet('background-color : lightblue')

        # Push Button
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('ADD TASK')
        self.pushb.setStyleSheet('color : white; background-color : black')
        font = QFont('Times')
        font.setBold(True)
        font.setPointSize(12)
        self.pushb.setFont(font)

        # Output
        self.out.setFrameShape(QFrame.Shape.Box)
        self.out.setAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.out.setGeometry(out_x, out_y, out_width, out_height)
        self.out.setStyleSheet('Background-color : white')

        # Set Signal
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    # 5 Set Event
    def Events(self):
        global Tasks
        Task = self.line.text()
        appointment = self.cal.selectedDate().toString('yyyy-mm-dd')
        Tasks = Tasks + f'\n {Task} on {appointment}'
        self.out.setText(Tasks)



# 6 Execute Application
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
