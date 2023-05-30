# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 800
dlg_height = 600

# Title Geometry
title_width = 200
title_height = 20
title_x = int((dlg_width / 2) - (title_width / 2)) + 40
title_y = 20

# Task Geometry
task_width = 100
task_height = 20
task_x = 10
task_y = title_y + 40

line_width = 100
line_height = 20
line_x = (task_x + task_width) + 10
line_y = task_y - 3

# Calendar Geometry
cal_width = 300
cal_height = 300
cal_x = line_x - 50
cal_y = line_y + 50

# Button Geometry
add_width = 200
add_height = 40
add_x = line_x + 5
add_y = (cal_y + cal_height) + 48

# ListView Geometry
list_width = 300
list_height = 300
list_x = cal_x + cal_width + 70
list_y = cal_y

# Delete Task Geometry
del_width = 200
del_height = 40
del_x = list_x + \
        int((list_width / 2)) - \
        int((del_width / 2))
del_y = cal_y + cal_height + 50

class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Task Manager')

        # Define Field
        self.title = None
        self.task = None
        self.line = None
        self.cal = None
        self.add = None
        self.Del = None
        self.List = None
        self.out = None
        self.model = None

    # 4 Create Widgets
    def Widgets(self):
        self.title = QLabel(self.dialog)
        self.task = QLabel(self.dialog)
        self.line = QLineEdit(self.dialog)
        self.cal = QCalendarWidget(self.dialog)
        self.add = QPushButton(self.dialog)
        self.Del = QPushButton(self.dialog)
        self.List = QListView(self.dialog)
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

        # Add Task
        self.add.setGeometry(add_x, add_y, add_width, add_height)
        self.add.setText('ADD TASK')
        self.add.setStyleSheet('color: White; background-color : Black')

        # Delete Task
        self.Del.setGeometry(del_x, del_y, del_width, del_height)
        self.Del.setText('DELETE TASK')
        self.Del.setStyleSheet('color: White; background-color : Black')

        # ListView
        self.List.setGeometry(list_x, list_y, list_width, list_height)
        self.List.setFrameShape(QFrame.Shape.WinPanel)
        self.model = QStandardItemModel(self.List)

        # Set Slot & signals
        self.add.clicked.connect(self.add_task)
        self.Del.clicked.connect(self.del_task)
        QMetaObject.connectSlotsByName(self.dialog)

    # 4 Set Events
    def add_task(self):
        Task = self.line.text()
        appointment = self.cal.selectedDate().toString("yyyy-MM-dd")
        item = QStandardItem(f'{Task} on {appointment}')

        self.model.appendRow(item)
        self.List.setModel(self.model)

    def del_task(self):
        Tasks = self.List.selectedIndexes()
        for char in Tasks:
            self.model.removeRow(char.row())



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
