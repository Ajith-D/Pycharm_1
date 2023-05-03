# 1 Import Libraries
import sys
from PyQt6 import QtGui, QtCore, QtWidgets


# 2 Create One Class
class ApplicationForm:
    # 3 set dialog
    def __init__(self, form):
        self.dialog = form
        self.dialog.setObjectName("Dialog")
        self.dialog.resize(350, 250)
        # True is a Boolean, don't enter as a string
        self.dialog.setEnabled(True)
        self.dialog.setWindowTitle("Ajith")

        # Give the introduction about widgets on constructor itself
        self.lb_title = None
        self.PushB = None

    # 4  Set Widgets
    def setup_Widgets(self):

        # Label
        self.lb_title = QtWidgets.QLabel(self.dialog)
        self.lb_title.setObjectName("Label")
        self.lb_title.setGeometry(125, 90, 130, 30)
        self.lb_title.setText('Hello !')

        # Push Button
        self.PushB = QtWidgets.QPushButton(self.dialog)
        self.PushB.setObjectName("Button")
        self.PushB.setGeometry(120, 120, 150, 30)
        self.PushB.setText("Welcome")

        # Set Signal
        self.PushB.clicked.connect(self.Event)

        # Set Slot
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    # 5 set Events
    def Event(self):
        # To change the text of the Label use 'lb_title' function
        self.lb_title.setText("Iam Learning PyCharm")


# Execute Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QWidget()

    # Give the form class
    userI = ApplicationForm(App)

    # Initialize the Widget
    userI.setup_Widgets()

    # Show Form
    App.show()

    # Close the Form
    sys.exit(app.exec())
