# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import pandas as pd
#from AatomzTable import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 760
dlg_height = 550

# Title Geometry
title_width = 200
title_height = 20
title_x = int((dlg_width / 2) - (title_width / 2)) + 40
title_y = 20

# Task Geometry
task_width = 160
task_height = 20
task_x = -30
task_y = title_y + 40

line_width = 200
line_height = 20
line_x = (task_x + task_width) + 10
line_y = task_y

# Calendar Geometry
cal_width = 300
cal_height = 300
cal_x = line_x - 90
cal_y = line_y + 50

# Button Geometry
add_width = 200
add_height = 40
add_x = line_x - 40
add_y = (cal_y + cal_height) + 48

# ListView Geometry
tv_width = 300
tv_height = 300
tv_x = cal_x + cal_width + 60
tv_y = cal_y

Tasks = []

# 3 Set class
class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Task Manager')
        self.dialog.setStyleSheet('background-color : #336666')

        # Define Field
        self.title = None
        self.task = None
        self.line = None
        self.cal = None
        self.add = None
        self.table = None
        self.out = None
        self.model = None

    # 4 Create Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.task = QLabel(self.dialog)
        self.line = QLineEdit(self.dialog)
        self.cal = QCalendarWidget(self.dialog)
        self.add = QPushButton(self.dialog)
        self.table = QTableView(self.dialog)
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
        self.task.setStyleSheet('color: white')
        font = QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        self.task.setFont(font)

        # Line
        self.line.setGeometry(line_x, line_y, line_width, line_height)
        self.line.setStyleSheet('background-color: white')

        # Calender
        self.cal.setGeometry(cal_x, cal_y, cal_width, cal_height)
        self.cal.setGridVisible(True)
        self.cal.setMinimumDate(QDate.currentDate())
        self.cal.setStyleSheet('background-color : white')

        # Add Task
        self.add.setGeometry(add_x, add_y, add_width, add_height)
        self.add.setText('ADD TASK')
        self.add.setStyleSheet('color: White; background-color : Black')
        font = QFont('Times')
        font.setBold(True)
        self.add.setFont(font)

        # Table View
        self.table.setGeometry(tv_x, tv_y, tv_width, tv_height)
        self.table.setFrameShape(QFrame.Shape.WinPanel)
        self.table.setStyleSheet('background-color: white')

        # Set Slot & signals
        self.add.clicked.connect(self.add_task)
        QMetaObject.connectSlotsByName(self.dialog)

    def add_task(self):
        Task = self.line.text()
        appointment = self.cal.selectedDate().toString("yyyy-mm-dd")
        Tasks.append([Task, appointment])
        df = pd.DataFrame(Tasks, columns=['Task', 'Date'],
                      index=range(1, len(Tasks) + 1))
        self.model = AtomzTable(df)
        self.table.setModel(self.model)


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
