from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame, QTableWidget, QPushButton
from PySide6.QtCore import Qt
from views.mainwindow import MainWindow
import pickle as pk
from os import path

class MainWindowForm (QWidget, MainWindow):
    def __init__ (self) -> None:
        super().__init__()
        self.setupUi (self)

        # self.createFile ()
        self.loadState ()

        self.nombre_textEdit.textChanged.connect (self.textoModificado)
        self.codigo_textEdit.textChanged.connect (self.textoModificado)
        self.correo_textEdit.textChanged.connect (self.textoModificado)
        self.carrera_textEdit.textChanged.connect (self.textoModificado)

    def saveState (self) -> None:
        nombre = str (self.nombre_textEdit.toPlainText ())
        codigo = str (self.codigo_textEdit.toPlainText ())
        correo = str (self.correo_textEdit.toPlainText ())
        carrera = str (self.carrera_textEdit.toPlainText ())

        diccionario = {
            "nombre": nombre,
            "codigo": codigo,
            "correo": correo,
            "carrera": carrera 
        }

        with open ("checkpoint.pickle", 'wb+') as archivo:
            pk.dump (diccionario, archivo)

    def loadState (self) -> None:
        if not path.exists ("checkpoint.pickle"):
            return
        
        diccionario = {}

        with open ("checkpoint.pickle", 'rb+') as archivo:
            diccionario = pk.load (archivo)
        
        for key, value in diccionario.items ():
            if (key == "nombre"):
                self.nombre_textEdit.setPlainText (value)
            elif (key == "codigo"):
                self.codigo_textEdit.setPlainText (value)
            elif (key == "correo"):
                self.correo_textEdit.setPlainText (value)
            elif (key == "carrera"):
                self.carrera_textEdit.setPlainText (value)
    
    def textoModificado (self):
        self.saveState ()
