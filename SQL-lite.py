import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sqlite3


class AppForm:
    def __int__(self, form):
        #form = QWidget
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

        #Set Signal
        self.students.selectionModel().selectionChanged.connect(self.load)
        self.pb_register.clicked.connect(self.register)
        self.pb_update.clicked.connect(self.update)
        self.pb_delete.clicked.connect(self.delete)

        QMetaObject.connectSlotsByName(self.dialog)

    def select(self):
        self.model.clear()
        items = self.db.execute(f"SELECT * FROM students").fetchall()
        for item in items:
            id = QStandardItemModel(str(item[0]))
            self.model.appendRow(id)

    def register(self):
        items = self.db.execute(f"""SELECT * FROM students
        WHERE id = {self.id.text()}""").fetchall()

    def delete(self):
        id = int(self.id.text())
        self.db.execute(f"DELETE FROM students WHERE id={id}")
        self.connection.commit()
        self.select()

    def load(self, selected, deselection):

        indexes = selected.indexes()
        if indexes:
            selected_indexes = indexes[0]
            selected_item = str(self.model.data(selected_indexes))
            items = self.db.execute(f"""SELECT * FROM students
            WHERE id = {selected_item}""").fetchall()
            if len(items) > 0:
                id = str(items[0][0])
                name = str(items[0][1])
                age = str(items[0][2])
                joined = str(items[0][3])
                completed = str(items[0][4])
                city = str(items[0][5])

                self.id_line.setText(id)
                self.name_le.setText(name)
                self.age_le.setText(age)
                self.join_le.setText(joined)
                self.complete_le.setText(completed)
                self.city_le.setText(city)

    def update(self):
        query = f"SELECt * FROM students WHERE id = {int(self.id_line.text())}"
        items = self.db.execute(query).fetchall()
        if len(items) == 1:
            query = f"""
            UPDATE students SEt name = '{self.name_le.text()}',
            age = '{self.age_le.text()}', joined = '{self.join_le.text()}',
            completed = '{self.complete_le.text()}', city = '{self.city_le.text()}'
            WHERE id = {self.id_line.text()}"""
            print(query)
            self.db.execute(query)
            self.connection.commit()
        else:
            self.register()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = AppForm(Form)
    ui.widget()
    Form.show()
    sys.exit(app.exec())