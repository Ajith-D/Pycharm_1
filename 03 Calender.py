# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 500
dlg_height = 600

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

line_width = 100
line_height = 25
line_x = (task_x + task_width) + 10
line_y = task_y - 3

# Calendar Geometry
cal_width = 300
cal_height = 300
cal_x = int((dlg_width / 2) - (cal_width / 2))
cal_y = line_y + 50

# Button Geometry
pushb_width = 200
pushb_height = 40
pushb_x = int((dlg_width / 2) - (pushb_width / 2))
pushb_y = (cal_y + cal_height) + 10

# Output Geometry
out_width = 400
out_height = 50
out_x = 160
out_y = (pushb_y + pushb_height) + 20

# 3 Create Class
class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Task Manager')
        self.dialog.setStyleSheet('background-color : lightgrey')

        # Define Field
        self.title = None
        self.task = None
        self.line = None
        self.cal = None
        self.pushb = None
        self.out = None

     # 4 Create Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.task = QLabel(self.dialog)
        self.line = QLineEdit(self.dialog)
        self.cal = QCalendarWidget(self.dialog)
        self.pushb = QPushButton(self.dialog)
        self.out = QLabel(self.dialog)

        # Title
        self.title.setObjectName('Task')
        self.title.setText('Task Manager')
        self.title.setGeometry(title_x, title_y, title_width, title_height)
        font = QFont('Times')
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setItalic(True)
        self.title.setFont(font)

        # Task
        self.task.setGeometry(task_x, task_y, task_width, task_height)
        self.task.setText('Task: ')
        self.task.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Line
        self.line.setGeometry(line_x, line_y, line_width, line_height)
        self.line.setStyleSheet('background-color: white')

        # Calender
        self.cal.setGeometry(cal_x, cal_y, cal_width, cal_height)
        self.cal.setGridVisible(True)
        self.cal.setMinimumDate(QDate.currentDate())

        # PushButton
        self.pushb.setObjectName('Button')
        self.pushb.setGeometry(pushb_x, pushb_y, pushb_width, pushb_height)
        self.pushb.setText('ADD TASK')
        self.pushb.setStyleSheet('color: White; background-color : Black')

        # Output
        self.out.setGeometry(out_x, out_y, out_width, out_height)

        # Set Signal
        self.pushb.clicked.connect(self.Events)
        QMetaObject.connectSlotsByName(self.dialog)

    def Events(self):
        Task = self.line.text()
        appointment = self.cal.selectedDate().toString("yyyy-MM-dd")
        self.out.setText(f'{Task} on {appointment}')


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
