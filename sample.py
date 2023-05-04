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
        self.dialog.setWindowTitle("Ajith")

        # Give the introduction about widgets on constructor itself
        self.lb_title = None
        self.push = None

    # 4 Set Widgets
    def widgets(self):
        # Label
        self.lb_title = QtWidgets.QLabel(self.dialog)
        self.lb_title.setObjectName("Label")
        self.lb_title.setGeometry(200, 140, 130, 30)
        self.lb_title.setText("Hello")

        # Push Button
        self.push = QtWidgets.QPushButton(self.dialog)
        self.push.setObjectName("Button")
        self.push.setGeometry(150, 170, 130, 30)
        self.push.setText("Welcome")

        # Set Signal
        self.push.clicked.connect(self.Execute)
        # Set Slot
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    # 5 Set Events
    def Execute(self):
        self.lb_title.setText("Learning PyCharm")


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
