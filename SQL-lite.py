import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sqlite3

class AppForm:
    def __int__(self, form):
        self.dialog = form
        self.dialog.setWindowTitle('Python SQLite')
        self.dialog.setStylesheet('background-color : black; color : white')

        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.v1 = QVBoxLayout()
        self.v2 = QVBoxLayout()
        self.title = QLabel()
        self.id = QLabel()
        self.id_line = QLineEdit()
        self.name = QLabel()
        self.name_le = QLineEdit()
        self.age = QLabel()
        self.age_le = QLineEdit()
        self.join = QLabel()
        self.join_le = QLineEdit()
        self.complete = QLabel()
        self.complete_le = QLineEdit()
        self.city = QLabel()
        self.city_le = QLineEdit()
        self.students = QListView()
        self.model = QStandardItemModel(self.students)
        self.pb_register = QPushButton()
        self.pb_update = QPushButton()
        self.pb_delete = QPushButton()
        self.pb_new = QPushButton()

        #For Database Connectivity
        self.connection = sqlite3.connect('Ajith.db')
        self.db = self.connection.cursor()

    def widget(self):
        self.title.setText('Registration')
        self.id.setText('Register No: ')
        self.name.setText('Name: ')
        self.age.setText('Age: ')
        self.join.setText('Joined:')
        self.complete.setText('Completed: ')
        self.city.setText('City: ')
        self.students.setStyleSheet('background-color:#a22d75; color:white')
        self.pb_register.setText('Register')
        self.pb_register.setStyleSheet('background-color:#a22d75; color:white')
        self.pb_update.setText('Update')
        self.pb_update.setStyleSheet('background-color:#a22d75; color:white')
        self.pb_delete.setText('Delete')
        self.pb_delete.setStyleSheet('background-color:#a22d75; color:white')
        self.pb_new.setText('New')
        self.pb_new.setStyleSheet('background-color:#a22d75; color:white')

        # Layout
        self.v1.addWidget(self.title)
        self.v1.addWidget(self.id)
        self.v1.addWidget(self.id_line)
        self.v1.addWidget(self.name)
        self.v1.addWidget(self.name_le)
        self.v1.addWidget(self.age)
        self.v1.addWidget(self.age_le)
        self.v1.addWidget(self.join)
        self.v1.addWidget(self.join_le)
        self.v1.addWidget(self.complete)
        self.v1.addWidget(self.complete_le)
        self.v1.addWidget(self.city)
        self.v1.addWidget(self.city_le)
        self.v1.addWidget(self.h2)
        self.v1.addStretch()
        self.v2.addWidget(self.students)

        self.h1.addLayout(self.v1)
        self.h1.addLayout(self.v2)

        self.h2.addWidget(self.pb_register)
        self.h2.addWidget(self.pb_update)
        self.h2.addWidget(self.pb_delete)
        self.h2.addWidget(self.pb_new)

        self.dialog.setLayout(self.h1)

        self.select()
        self.students.setModel(self.model)

    def select(self):

    def register(self):

    def delete(self):

    def load(self):

    def update(self):


def main():


if __name__ == '__main__':
    main()