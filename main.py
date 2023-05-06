# 1 Import Libraries
import sys
from PyQt6 import QtGui, QtCore, QtWidgets


# 2 Create One Class
class ApplicationForm:
    # 3 Set Dialog
    def __init__(self, form):
        self.dialog = QtWidgets.QWidget()
        self.dialog.setObjectName("MyApp")

        # Set Widget Properties
        self.dialog.setEnabled(True)
        self.dialog.setGeometry(100, 100, 500, 50)
        #Set Handling Size
        self.dialog.setMaximumSize(400, 150)
        self.dialog.setMinimumSize(200, 100)
        #self.dialog.resize(450, 390)
        self.dialog.setWindowTitle("Ajith")
        self.dialog.setWindowOpacity(1.0)

        # Set tooltip - like DocString
        self.dialog.setToolTip('This is main window')

        # Set Cursor
        #Cursor = QtGui.QCursor(QtCore.Qt.ArrowType)
        # self.dialog.setCursor(Cursor)

        # Define Fields
        self.label1 = None
        self.label2 = None
        self.pushb = None

    # 4 Set Widgets
    def widgets(self):
        # Setting QObject Properties
        self.dialog.setObjectName("MyApp")

        self.label1 = QtWidgets.QLabel(self.dialog)
        self.label2 = QtWidgets.QLabel(self.dialog)

        # Label 1
        self.label1.setEnabled(True)
        self.label1.setObjectName("Label")
        self.label1.setGeometry(155, 140, 130, 30)
        self.label1.setStyleSheet("background-color: transparent")
        self.label1.setText("Hello!")

        # Set Tool tip for Label 1
        self.label1.setToolTip('Hello Label 1')

        # Set Font For Label1
        font = QtGui.QFont('Times')
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(18)
        self.label1.setFont(font)

        # Set QFrame Property
        #self.label1.setFrameShape(QtWidgets.QFrame.frameShape('Box'))

        # Set QLabel Properties
        self.label1.setText("Hello label1")
        # self.label1.setAlignment(QtCore.Qt.)
        # self.label1.setAlignment(QtCore.Qt.)
        self.label1.setMargin(2)

        # Set Cursor for Label 1
        #Cursor = QtGui.QCursor(QtCore.Qt.Ope)
        #self.label1.setCursor(Cursor)

        # Label 2
        self.label2.setEnabled(True)
        self.label2.setObjectName("Label")
        self.label2.setGeometry(155, 140, 130, 30)
        self.label2.setStyleSheet("background-color: transparent")
        self.label2.setText("Hello!")

        # Set Tool tip for Label 2
        self.label2.setToolTip('Hello Label 2')

        # Set Font For Label2
        font = QtGui.QFont('Times')
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(20)
        self.label2.setFont(font)


        # Set Cursor for Label 2
        #Cursor = QtGui.QCursor(QtCore.Qt.)
        # self.label2.setCursor(Cursor)


        # Push Button
        self.pushb = QtWidgets.QPushButton(self.dialog)
        self.pushb.setObjectName("Button")
        self.pushb.setGeometry(150, 170, 160, 30)
        self.pushb.setText("Welcome")

        # Set Signal
        self.pushb.clicked.connect(self.Event)

        # Set Slot
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    # 5 Set Events
    def Event(self):
        self.label1.setText("Learning PyCharm")


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
