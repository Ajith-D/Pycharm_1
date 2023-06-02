# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

# 2 Set Constant Values
# Dialog Geometry
dlg_width = 400
dlg_height = 400

# 3 Set class
class AppForm:
    def __init__(self, form):
        #form = QWidget()
        self.dialog = form
        self.dialog.setGeometry(100, 100, dlg_width, dlg_height)
        self.dialog.setWindowTitle('Button')
        self.dialog.setStyleSheet('background-color : #336666')

        #Set Field
        self.pb_top = None
        self.pb_bottom = None
        self.pb_center = None
        self.placement = None
        self.layout = None

    # 4 Create Widgets
    def Widgets(self):
        self.pb_top = QPushButton(self.dialog)
        self.pb_top.setText('TOP')
        self.pb_top.setStyleSheet('color: White; background-color : Black')

        self.pb_center = QPushButton(self.dialog)
        self.pb_center.setText('CENTER')
        self.pb_center.setStyleSheet('color: White; background-color : Black')

        self.pb_bottom = QPushButton(self.dialog)
        self.pb_bottom.setText('BOTTOM')
        self.pb_bottom.setStyleSheet('color: White; background-color : Black')

        self.placement = QWidget(self.dialog)
        self.layout = QVBoxLayout(self.dialog)
        self.placement.setGeometry(0, 0, 300, 100)

        self.layout.addWidget(self.pb_top)
        self.layout.addWidget(self.pb_center)
        self.layout.addWidget(self.pb_bottom)
        self.dialog.setLayout(self.layout)



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
