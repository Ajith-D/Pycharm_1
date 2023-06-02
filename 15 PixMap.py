# 1 Import Libraries
import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 900
dlg_height = 600

# 3 Set class
class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Task Manager')
        self.dialog.setStyleSheet('background-color : #336666')

        self.logo1 = None
        self.logo2 = None
        self.logo3 = None
        self.logo4 = None

        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None

        self.placement1 = None
        self.placement2 = None
        self.hlayout = None
        self.vlayout = None

    def Widgets(self):
        # Set Pixmap & Label
        self.logo1 = QPixmap(r"C:\Users\User\Desktop\course\New folder\default-share.png")
        self.label1 = QLabel(self.dialog)
        self.label1.setPixmap(self.logo1)

        self.logo2 = QPixmap(r"C:\Users\User\Desktop\course\New folder\displaying-19-gallery-images-for-linkedin-logo-png-25.png")
        self.label2 = QLabel(self.dialog)
        self.label2.setPixmap(self.logo2)

        self.logo3 = QPixmap(r"C:\Users\User\Desktop\course\New folder\download.png")
        self.label3 = QLabel(self.dialog)
        self.label3.setPixmap(self.logo3)

        self.logo4 = QPixmap(r"C:\Users\User\Desktop\course\New folder\images.png")
        self.label4 = QLabel(self.dialog)
        self.label4.setPixmap(self.logo4)

        # Set Placement 1
        self.placement1 = QWidget(self.dialog)
        self.placement1.setGeometry(0, 10, 300, 500)
        self.placement1.setStyleSheet('background-color : #66FF99')
        self.vlayout = QVBoxLayout(self.dialog)
        self.vlayout.addWidget(self.label1)
        self.vlayout.addWidget(self.label2)
        self.placement1.setLayout(self.vlayout)

        # Set Placement2
        self.placement2 = QWidget(self.dialog)
        self.placement2.setGeometry(300, 0, 500, 260)
        self.placement2.setStyleSheet('background-color : #666')
        self.hlayout = QHBoxLayout(self.dialog)
        self.hlayout.addWidget(self.label3)
        self.hlayout.addWidget(self.label4)
        self.placement2.setLayout(self.hlayout)


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
