from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class Wnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0)
        self.setGraphicsEffect(self.shadow)


        self.wW = QWebEngineView(self)
        self.wW.setGeometry(100, 100, 300, 300)
        self.url = QUrl("https://evileg.com/ru/forum/topic/623/")
        self.wW.load(self.url)
        self.wW.show()

        self.wW.close = QPushButton(self)
        self.wW.close.resize(20, 20)
        self.wW.close.move(380, 100)
        self.wW.close.setText("X")
        self.wW.close.clicked.connect(self.close)

    def mouseMoveEvent(self, event):
        if event.button() == Qt.LeftButton:
            pass


if __name__ == "__main__":
    app = QApplication([])
    wnd = Wnd()
    wnd.show()
    sys.exit(app.exec())
