from PyQt5.QtCore import Qt, QUrl, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QLinearGradient, QColor
from views.QTBrowserWindow import Ui_BackgroundForm
from views import StyleSheethHelper
import sys


class Wnd(QWidget, Ui_BackgroundForm):
    def __init__(self):
        super().__init__()

        self.is_pressed = False
        self.old_pos = QPoint(0, 0)
        self.url = QUrl("https://evileg.com/ru/forum/topic/623/")

        self.setupUi(self)
        self.setWindowIcon(QIcon("./static/images/menu.png"))
        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)
        self.btnMaximize.clicked.connect(self.btnMaximizeController)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = True
            self.old_pos = event.globalPos()

            if self.isMaximized():
                self.showNormal()

    def mouseMoveEvent(self, event):
        if self.is_pressed:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = False

            if event.globalPos().y() == 0:
                self.showMaximized()

    def btnMaximizeController(self):
        if self.isMaximized():
            self.showNormal()
            self.btnMaximize.setIcon(QIcon("./static/images/maximize.png"))
            self.Form.setStyleSheet(StyleSheethHelper.formFormStyleSheet_normal)
            self.btnQtMenu.setStyleSheet(StyleSheethHelper.btnQtMenuStyleSheet_normal)
            return
        self.showMaximized()
        self.btnMaximize.setIcon(QIcon("./static/images/minimize.png"))
        self.Form.setStyleSheet(StyleSheethHelper.formFormStyleSheet_maximized)
        self.btnQtMenu.setStyleSheet(StyleSheethHelper.btnQtMenuStyleSheet_maximized)


if __name__ == "__main__":
    app = QApplication([])
    wnd = Wnd()
    wnd.show()
    sys.exit(app.exec())
