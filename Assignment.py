# 1 Import Libraries
import sys
from PyQt6 import QtGui, QtCore, QtWidgets


# 2 Create One Class
class ApplicationForm:
    # 3 Set Dialog
    def __init__(self, form):
        self.dialog = form
        self.dialog.setObjectName("Dialog")
        self.dialog.setEnabled(True)
        self.dialog.resize(450, 390)
        self.dialog.setWindowTitle("My Window App")

        # Give the introduction about widgets on constructor itself
        self.lb_title = None
        self.pushb1 = None
        self.pushb2 = None

    # 4 Set Widgets
    def widgets(self):
        # Label
        self.lb_title = QtWidgets.QLabel(self.dialog)
        self.lb_title.setObjectName("Label")
        self.lb_title.setGeometry(190, 90, 130, 30)
        self.lb_title.setText("Set Some Text")

        # Push Button1
        self.pushb1 = QtWidgets.QPushButton(self.dialog)
        self.pushb1.setObjectName("Button1")
        self.pushb1.setGeometry(70, 150, 100, 30)
        self.pushb1.setText("Hello")

        # Push Button2
        self.pushb2 = QtWidgets.QPushButton(self.dialog)
        self.pushb2.setObjectName("Button2")
        self.pushb2.setGeometry(270, 150, 100, 30)
        self.pushb2.setText("World")


        # Set Signal
        self.pushb1.clicked.connect(self.Event1)
        self.pushb2.clicked.connect(self.Event2)

        # Set Slot
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    # 5 Set Events
    def Event1(self):
        self.lb_title.setText("Set Hello")
    def Event2(self):
        self.lb_title.setText("Set World")


# Execute Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QWidget()

    # Give the form class
    userI = ApplicationForm(App)

    # Initialize the Widget
    userI.widgets()

    # Show Form
    App.show()

    # Close the Form
    sys.exit(app.exec())
