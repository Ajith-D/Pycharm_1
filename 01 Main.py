#  Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

# 1 Create Class
class AppForm:
    def __init__(self, form):
        #form = QtWidgets.QWidget()
        self.dialog = form
        self.dialog.setObjectName("My App")
        self.dialog.setEnabled(True)
        self.dialog.resize(550, 500)
        self.dialog.setWindowTitle("My Window")
        self.dialog.setWindowOpacity(1.0)
        # Set Handling Size
        self.dialog.setMaximumSize(700, 500)
        self.dialog.setMinimumSize(300, 180)

        #set ToolTip
        self.dialog.setToolTip('This is Main Window')

        # Set Font Control for Dialog
        font = QFont('Times')
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.dialog.setFont(font)

        #Define Fields
        self.label1 = None
        self.label2 = None
        self.pushb = None

    # 2 Create Widget
    def Widgets(self):
        # 1 set QObject Properties
        self.label1 = QLabel(self.dialog)
        self.label2 = QLabel(self.dialog)
        self.pushb = QPushButton(self.dialog)

        # Label 1
        self.label1.setObjectName("Label 1")
        self.label1.setEnabled(True)
        self.label1.setGeometry(180, 120, 175, 40)
        self.label1.setText("Hello Label 1")
        self.label1.setStyleSheet("color: White; background-color: Black")
        self.label1.setToolTip('This is Label 1')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setMargin(1)
        # Set Tool Tip for Label 1
        self.label1.setToolTip('This is Label 1')

        #Set Font For Label 1
        font = QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label1.setFont(font)

        #Set QFrame Property
        self.label1.setFrameShape(QFrame.Shape.Box)

        # Set Cursor
        Cursor = QCursor(Qt.CursorShape.PointingHandCursor)
        self.label1.setCursor(Cursor)

        # Label 2
        self.label2.setObjectName("Label 2")
        self.label2.setEnabled(True)
        self.label2.setGeometry(180, 180, 175, 40)
        self.label2.setText("Hello Label 2")
        self.label2.setStyleSheet("color: White; background-color: Black")
        self.label2.setToolTip('This is Label 2')
        self.label2.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label2.setMargin(2)
        # Set Tool Tip for Label 2
        self.label2.setToolTip('This is Label 2')

        #Set Font For Label 2
        font = QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label2.setFont(font)

        # Set QFrame Property
        self.label2.setFrameShape(QFrame.Shape.Box)

        # Set Cursor
        Cursor = QCursor(Qt.CursorShape.ArrowCursor)
        self.label2.setCursor(Cursor)

        # Push Button
        self.pushb.setObjectName("Button")
        self.pushb.setGeometry(205, 240, 120, 30)
        self.pushb.setStyleSheet("background-color: lightgrey ")
        self.pushb.setText("Hello")

        # Set Signal
        self.pushb.clicked.connect(self.Event)
        # Set Slot
        QMetaObject.connectSlotsByName(self.dialog)

    # 3 Set Events
    def Event(self):
        self.label1.setText("Set Hello")


# 4 Execute Application
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
