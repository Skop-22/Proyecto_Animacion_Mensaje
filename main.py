from GUI.ui_untitled import *
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
import sys

class windowPrin(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.Prin = Ui_Dialog()
        self.Prin.setupUi(self)
        #----------------------------------
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #---------------------------------
        self.Prin.Cerrar.clicked.connect(lambda: self.close())
        with open("CSS/styles.css","r") as f:
            self.setStyleSheet(f.read())
        self.AniMa()
        self.show()

    def AniMa(self):
        self.Animacion= QPropertyAnimation(self.Prin.widget, b'geometry')
        self.Animacion.setDuration(100)
        self.Animacion.setStartValue(QRect(0,100,470,0))
        self.Animacion.setEndValue(QRect(0,0,470,200))
        self.Animacion.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= windowPrin()
    sys.exit(app.exec())
