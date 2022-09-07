from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 620)
        MainWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CentralWidgetFrame = QFrame(MainWindow)
        self.CentralWidgetFrame.setObjectName(u"CentralWidgetFrame")
        self.CentralWidgetFrame.setFrameShape(QFrame.StyledPanel)
        self.CentralWidgetFrame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.CentralWidgetFrame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.BackgroundFrame = QFrame(self.CentralWidgetFrame)
        self.BackgroundFrame.setObjectName(u"BackgroundFrame")
        self.BackgroundFrame.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.BackgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.BackgroundFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ContentFrame = QFrame(self.BackgroundFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        self.ContentFrame.setFrameShape(QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QFrame.Raised)
        self.nombre = QLabel(self.ContentFrame)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(360, 40, 81, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.nombre.setFont(font)
        self.nombre.setStyleSheet(u"text-align: center")
        self.nombre_textEdit = QTextEdit(self.ContentFrame)
        self.nombre_textEdit.setObjectName(u"nombre_textEdit")
        self.nombre_textEdit.setGeometry(QRect(290, 90, 211, 31))
        self.nombre_textEdit.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.codigo_textEdit = QTextEdit(self.ContentFrame)
        self.codigo_textEdit.setObjectName(u"codigo_textEdit")
        self.codigo_textEdit.setGeometry(QRect(290, 180, 211, 31))
        self.codigo_textEdit.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.codigo = QLabel(self.ContentFrame)
        self.codigo.setObjectName(u"codigo")
        self.codigo.setGeometry(QRect(360, 130, 81, 31))
        self.codigo.setFont(font)
        self.codigo.setStyleSheet(u"text-align: center")
        self.correo = QLabel(self.ContentFrame)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(360, 220, 81, 31))
        self.correo.setFont(font)
        self.correo.setStyleSheet(u"text-align: center")
        self.correo_textEdit = QTextEdit(self.ContentFrame)
        self.correo_textEdit.setObjectName(u"correo_textEdit")
        self.correo_textEdit.setGeometry(QRect(290, 270, 211, 31))
        self.correo_textEdit.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.carrera_textEdit = QTextEdit(self.ContentFrame)
        self.carrera_textEdit.setObjectName(u"carrera_textEdit")
        self.carrera_textEdit.setGeometry(QRect(290, 370, 211, 31))
        self.carrera_textEdit.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.carrera = QLabel(self.ContentFrame)
        self.carrera.setObjectName(u"carrera")
        self.carrera.setGeometry(QRect(360, 320, 81, 31))
        self.carrera.setFont(font)
        self.carrera.setStyleSheet(u"text-align: center")
        self.botonEnviar = QPushButton(self.ContentFrame)
        self.botonEnviar.setObjectName(u"botonEnviar")
        self.botonEnviar.setGeometry(QRect(330, 460, 131, 31))
        self.botonEnviar.setStyleSheet(u"background-color: rgb(188, 188, 188);")

        self.verticalLayout_3.addWidget(self.ContentFrame)


        self.shadow_layout.addWidget(self.BackgroundFrame)


        self.verticalLayout.addWidget(self.CentralWidgetFrame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.codigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.correo.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.carrera.setText(QCoreApplication.translate("MainWindow", u"Carrera", None))
        self.botonEnviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

