#1 Import Libraries
import sys
from PyQt6 import QtGui, QtCore, QtWidgets

#2 Create One Class
class ApplicationForm:
    # 3 set dialog
    def __init__(self, form):
        self.dialog = form
        self.dialog.setObjectName("Dialog")
        self.dialog.resize(350, 250)
        # True is a Boolean, dont enter as an string
        self.dialog.setEnabled(True)
        self.dialog.setWindowTitle("Ajith")

#Execute Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    App = QtWidgets.QWidget()

    #Give the form class
    userI = ApplicationForm(App)

    #Show Form
    App.show()

    #Close the Form
    sys.exit(app.exec())




