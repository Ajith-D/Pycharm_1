# 1 Import Libraries
import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

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
        self.dialog.setContentsMargins(70, 30, 70, 30)
        #self.dialog.setLayout(QtWidgets.QLayout)

        Cursor = QCursor(Qt.CursorShape.ArrowCursor)
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

        self.label1 = QLabel(self.dialog)
        self.label2 = QLabel(self.dialog)
        self.label3 = QLabel(self.dialog)
        self.label4 = QLabel(self.dialog)
        self.label5 = QLabel(self.dialog)
        self.label6 = QLabel(self.dialog)
        self.label7 = QLabel(self.dialog)
        self.label8 = QLabel(self.dialog)

        # Label 1
        self.label1.setEnabled(True)
        self.label1.setObjectName("Label")
        self.label1.setGeometry(130, 20, 230, 30)
        self.label1.setText("Label")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont('Times')
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        self.label1.setFont(font)

        # Label 2
        self.label2.setEnabled(True)
        self.label2.setObjectName("Label")
        self.label2.setGeometry(130, 50, 230, 30)
        self.label2.setText("Assignment")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont('Times')
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        self.label2.setFont(font)

        # Label 3
        self.label3.setEnabled(True)
        self.label3.setObjectName("Label")
        self.label3.setGeometry(40, 120, 130, 30)
        self.label3.setText("Label 1")
        self.label3.setStyleSheet("color: red")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        self.label3.setFont(font)

        # Label 4
        self.label4.setEnabled(True)
        self.label4.setObjectName("Label")
        self.label4.setGeometry(135, 160, 70, 30)
        self.label4.setText("Label 2")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label4.setStyleSheet("color: white; background-color : blue")

        font = QFont('Times')
        font.setPointSize(12)
        font.setBold(True)
        self.label4.setFont(font)

        # Label 5
        self.label5.setEnabled(True)
        self.label5.setObjectName("Label")
        self.label5.setGeometry(210, 200, 125, 20)
        self.label5.setText("Label 3")
        self.label5.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # Set QFrame Property
        self.label5.setFrameShape(QFrame.Shape.Box)
        self.label5.setStyleSheet("color: white; background-color: Red")

        font = QFont('Times')
        font.setPointSize(11)
        font.setBold(True)
        self.label5.setFont(font)

        # Label 6
        self.label6.setEnabled(True)
        self.label6.setObjectName("Label")
        self.label6.setGeometry(210, 250, 125, 20)
        self.label6.setText("Label 3")
        self.label6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Set QFrame Property
        self.label6.setFrameShape(QFrame.Shape.Box)
        self.label6.setStyleSheet("color: white; background-color: Red")

        font = QFont('Times')
        font.setPointSize(11)
        font.setBold(True)
        self.label6.setFont(font)

        # Label 7
        self.label7.setEnabled(True)
        self.label7.setObjectName("Label")
        self.label7.setGeometry(210, 300, 125, 20)
        self.label7.setText("Label 3")
        self.label7.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Set QFrame Property
        self.label7.setFrameShape(QFrame.Shape.Box)
        self.label7.setStyleSheet("color: white; background-color: Red")

        font = QFont('Times')
        font.setPointSize(11)
        font.setBold(True)
        self.label7.setFont(font)

        # Label 8
        self.label8.setEnabled(True)
        self.label8.setObjectName("Label")
        self.label8.setGeometry(300, 400, 150, 90)
        self.label8.setText("Final Label")
        self.label8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont('Times')
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.label8.setFont(font)

        # Set Slot
        QMetaObject.connectSlotsByName(self.dialog)


# Execute Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    App = QWidget()

    # Give the form class
    userI = ApplicationForm(App)

    # Initialize the Widget
    userI.widgets()

    # Show Form
    App.show()

    # Close the Form
    sys.exit(app.exec())