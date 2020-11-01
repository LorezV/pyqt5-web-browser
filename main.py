from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class Wnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(200, 200, 1200, 1200)
        self.lbl = QLabel(self)
        self.lbl.resize(150, 100)
        self.lbl.move(100, 100)
        self.lbl.setText("asdasd");
        self.setWindowFlag(Qt.WindowFullScreen)

    def keyPressEvent(self, event):
            if(event.key() == Qt.Key_F):
                self.lbl.setText("nnnnnnnnnnnnnnnnnnn")


if __name__ == "__main__":
    app = QApplication([])
    wnd = Wnd()
    wnd.show()
    sys.exit(app.exec())
