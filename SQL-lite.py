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
        self.line = QLineEdit()
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

    def select(self):

    def register(self):

    def delete(self):

    def load(self):

    def update(self):


def main():


if __name__ == '__main__':
    main()