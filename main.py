from PySide6.QtWidgets import QApplication
from controllers.mainwindow import MainWindowForm
import sys

if __name__ == "__main__":
    app = QApplication ()
    window = MainWindowForm ()

    window.show ()
 
    sys.exit (app.exec ())
