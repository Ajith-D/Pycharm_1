#1 Import Libraries
import sys
from PyQt6 import QtGui, QtCore, QtWidgets

#2 Create One Class
class ApplicationForm:
    # 3 set dialog
    def __init__(self, form):
        self.dialog = form
        self.dialog.setObjectName("Dialog")
        self.dialog.resize(250, 200)
        self.dialog.setEnabled(True)
        self.dialog.setWindowTitle("Ajith")

#Execute Application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()

    #Give the form class
    ui = ApplicationForm(form)



    #Show Form
    form.show()

    #Close the Form
    sys.exit(app.exec())




