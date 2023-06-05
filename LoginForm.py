# 1 Import Libraries
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class AppForm(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        # To set Margin
        layout.setContentsMargins(20, 20, 20, 20)
        # To set Space Between Widgets
        layout.setSpacing(10)
        self.setLayout(layout)

        title = QLabel('LOGIN FORM')
        layout.addWidget(title, 0, 1)

        user = QLabel('USERNAME: ')
        layout.addWidget(user, 1, 0)

        pwd = QLabel('PASSWORD: ')
        layout.addWidget(pwd, 2 , 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 1, 1, 1, 2)

        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input2, 2, 1, 1, 2)

        button1 = QPushButton("Register")
        layout.addWidget(button1, 3, 1)

        button2 = QPushButton("Login")
        button2.clicked.connect(self.login)
        layout.addWidget(button2, 3, 2)

    def login(self):
        if self.input1.text() == 'Ajith' and self.input2.text() == '12345':
            print('Username and Password are Correct')
        else:
            print('Invalid Username and Password')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Give the form class
    userI = AppForm()

    # Show Form
    userI.show()

    # Close the Form
    sys.exit(app.exec())
