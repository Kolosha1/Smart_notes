from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from ui import Ui_MainWindow
from random import*
import string
import json

class NoteWindow(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {}
        self.read_notes()
        self.connects()

    def connects(self):
        self.ui.listWidget.itemClicked.connect(self.show_note)
        self.ui.pushButton_2.clicked.connect(self.add_note)
        self.ui.pushButton.clicked.connect(self.save_note)
        self.ui.pushButton_3.clicked.connect(self.del_note)

    def read_notes(self):
        try:
            with open("notes.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {"Ваша перша замітка":{
                "текст": "Текст замітки" , "теги":[],
            }}
        self.ui.listWidget.addItems(self.notes)
    
    def show_note(self):
        name = self.ui.listWidget.selectedItems()[0].text()
        self.ui.lineEdit.setText(name)
        self.ui.textEdit.setText(self.notes[name]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[name]["теги"])
    
    def add_note(self):
        self.ui.lineEdit.clear()
        self.ui.textEdit.clear()
        self.ui.listWidget_2.clear()

    def save_file(self):
        try:
            with open("notes.json", "w", encoding="utf-8") as file:
                json.dump(self.notes, file, ensure_ascii=False)
        except:
            message = QMessageBox
            message.setText("Не вдалося зберегти")
            message.show()
            message.exec_()

    def save_note(self):
        title = self.ui.lineEdit.text()
        text = self.ui.textEdit.toPlainText()

        self.notes[title] = {"текст": text, "теги": []}
        self.save_file()
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.notes)

    def del_note(self):
        title = self.ui.lineEdit.text()
        if title in self.notes:
            del self.notes[title]
            self.save_file()
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.notes)
            self.add_note()






app = QApplication([])
ex = NoteWindow()
ex.show()
app.exec_()