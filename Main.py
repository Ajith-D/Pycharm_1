# 1 Import Libraries
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui

# 1 Create Class
class AppForm:
    def __init__(self, form):
        #form = QtWidgets.QWidget()
        self.dialog = form
        self.dialog.setObjectName("My App")
        self.dialog.setEnabled(True)
        self.dialog.resize(450, 390)
        self.dialog.setGeometry(QtCore.QRect(100, 100, 500, 40))
        self.dialog.setWindowTitle("My Window")
        self.dialog.setWindowOpacity(1.0)
        # Set Handling Size
        self.dialog.setMaximumSize(700, 500)
        self.dialog.setMinimumSize(300, 180)

        #set ToolTip
        self.dialog.setToolTip('This is Main Window')

        # Set Font Control
        #font = QtGui.QFont('Times')
        #font.setPointSize(18)
        #font.setBold(True)
        #font.setItalic(True)
        #font.setUnderline(True)
        #self.dialog.setFont(font)

        #Set Cursor
        #Cursor = QtGui.QCursor(QtCore.Qt.ArrowType)
        #self.dialog.setCursor(Cursor)

        #Define Fields
        self.pushb = None
        self.label1 = None
        self.label2 = None

    # 2 Create Widget
    def Widgets(self):
        # 1 set QObject Properties
        self.dialog.setObjectName("My App")

        self.label1 = QtWidgets.QLabel(self.dialog)
        self.label2 = QtWidgets.QLabel(self.dialog)

        # Label 1
        self.label1.setObjectName("Label 1")
        self.label1.setEnabled(True)
        self.label1.setGeometry(QtCore.QRect(50, 40, 175, 40))
        self.label1.setText("Hello Label 1")
        self.label1.setStyleSheet("background-color: transparent")
        self.label1.setToolTip('This is Label 1')

        # QLabel Properties
        self.label1.setText('Hello Label 1')
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.label1.setMargin(2)

        #Set Font For Label 1
        font = QtGui.QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label1.setFont(font)

        #Set QFrame Property
        self.label1.setFrameShape(QtWidgets.QFrame.Shape.Box)

        # Set Cursor
        #Cursor = QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor)
        #self.label1.setCursor(Cursor)

        # Label 2
        self.label2.setObjectName("Label 2")
        self.label2.setEnabled(True)
        self.label2.setGeometry(QtCore.QRect(70, 90, 175, 40))
        self.label2.setText("Hello Label 2")
        self.label2.setStyleSheet("background-color: transparent")
        self.label2.setToolTip('This is Label 2')

        #Set Font For Label 2
        font = QtGui.QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label2.setFont(font)

        # Set Cursor
        #Cursor = QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor)
        #self.label2.setCursor(Cursor)

        # Push Button
        self.pushb = QtWidgets.QPushButton(self.dialog)
        self.pushb.setObjectName("Button")
        self.pushb.setGeometry(QtCore.QRect(50, 200, 100, 30))
        self.pushb.setText("Hello")

        # Set Signal
        self.pushb.clicked.connect(self.Event)
        # Set Slot
        QtCore.QMetaObject.connectSlotsByName(self.dialog)


    # 3 Set Events
    def Event(self):
       self.label2.setText("Set Hello")

# 4 Execute Apllication
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    # Give the form class
    userI = AppForm(Form)

    # Initialize the Widget
    userI.Widgets()

    # Show Form
    Form.show()

    # Close the Form
    sys.exit(app.exec())















