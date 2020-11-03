from PyQt5.QtCore import Qt, QUrl, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from views.QTBrowserWindow import Ui_BackgroundForm
import sys
import os

print(os.getcwd())


class Wnd(QWidget, Ui_BackgroundForm):
    def __init__(self):
        super().__init__()

        self.is_pressed = False
        self.old_pos = QPoint(0, 0)

        self.setupUi(self)
        self.setWindowIcon(QIcon("./static/images/menu.png"))
        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnMaximize.clicked.connect(self.btnMaximizeController)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = True
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.is_pressed:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = False

    def btnMaximizeController(self):
        if self.isMaximized():
            self.showNormal()
            return
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication([])
    wnd = Wnd()
    wnd.show()
    sys.exit(app.exec())
