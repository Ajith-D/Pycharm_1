# 1 Import Libraries
import sys
from PyQt6 import QtGui, QtCore, QtWidgets


# 2 Create One Class
class ApplicationForm:
    # 3 Set Dialog
    def __init__(self, form):
        # Set Dialog
        self.dialog = form
        #self.dialog = QtWidgets.QWidget()
        self.dialog.setObjectName("Dialog")
        self.dialog.setEnabled(True)
        self.dialog.resize(500, 600)
        self.dialog.setWindowTitle("My Label Assignment")
        self.dialog.setMaximumSize(600, 500)
        self.dialog.setMinimumSize(400, 200)

        Cursor = QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor)
        self.dialog.setCursor(Cursor)

        # Define Fields
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.label5 = None
        self.label6 = None
        self.label7 = None
        self.label8 = None


    # 4 Set Widgets
    def widgets(self):

        self.label1 = QtWidgets.QLabel(self.dialog)
        self.label2 = QtWidgets.QLabel(self.dialog)
        self.label3 = QtWidgets.QLabel(self.dialog)
        self.label4 = QtWidgets.QLabel(self.dialog)
        self.label5 = QtWidgets.QLabel(self.dialog)
        self.label6 = QtWidgets.QLabel(self.dialog)
        self.label7 = QtWidgets.QLabel(self.dialog)
        self.label8 = QtWidgets.QLabel(self.dialog)

        # Label 1
        self.label1.setEnabled(True)
        self.label1.setObjectName("Label")
        self.label1.setGeometry(130, 20, 230, 30)
        self.label1.setText("Label")
        #self.label1.set
        self.label1.setAutoFillBackground(True)
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont('Times')
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label1.setFont(font)

        # Label 2
        self.label2.setEnabled(True)
        self.label2.setObjectName("Label")
        self.label2.setGeometry(130, 50, 230, 30)
        self.label2.setText("Assignment")
        self.label2.setAutoFillBackground(True)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont('Times')
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label2.setFont(font)

        # Label 3
        self.label3.setEnabled(True)
        self.label3.setObjectName("Label")
        self.label3.setGeometry(40, 120, 130, 30)
        self.label3.setText("Label 1")
        self.label3.setStyleSheet("color: red")
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label3.setFont(font)

        # Label 4
        self.label4.setEnabled(True)
        self.label4.setObjectName("Label")
        self.label4.setGeometry(135, 160, 70, 30)
        self.label4.setText("Label 2")
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label4.setStyleSheet("color: white; background-color : blue")

        font = QtGui.QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label4.setFont(font)

        # Label 5
        self.label5.setEnabled(True)
        self.label5.setObjectName("Label")
        self.label5.setGeometry(210, 200, 125, 20)
        self.label5.setText("Label 3")
        self.label5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        # Set QFrame Property
        self.label5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label5.setStyleSheet("color: white; background-color: Red")

        font = QtGui.QFont('Times')
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label5.setFont(font)

        # Label 6
        self.label6.setEnabled(True)
        self.label6.setObjectName("Label")
        self.label6.setGeometry(210, 250, 125, 20)
        self.label6.setText("Label 3")
        self.label6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # Set QFrame Property
        self.label6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label6.setStyleSheet("color: white; background-color: Red")

        font = QtGui.QFont('Times')
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label6.setFont(font)

        # Label 7
        self.label7.setEnabled(True)
        self.label7.setObjectName("Label")
        self.label7.setGeometry(210, 300, 125, 20)
        self.label7.setText("Label 3")
        self.label7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        # Set QFrame Property
        self.label7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label7.setStyleSheet("color: white; background-color: Red")

        font = QtGui.QFont('Times')
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label7.setFont(font)

        # Label 8
        self.label8.setEnabled(True)
        self.label8.setObjectName("Label")
        self.label8.setGeometry(300, 400, 150, 90)
        self.label8.setText("Final Label")
        self.label8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        font = QtGui.QFont('Times')
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.label8.setFont(font)

        # Push Button1
        #self.pushb1 = QtWidgets.QPushButton(self.dialog)
        #self.pushb1.setObjectName("Button1")
        #self.pushb1.setGeometry(70, 150, 100, 30)
        #self.pushb1.setText("Hello")

        # Set Signal
        #self.pushb1.clicked.connect(self.Event1)
        # Set Slot
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    # 5 Set Events
    #def Event1(self):
        #self.label1.setText("Set Hello")


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
