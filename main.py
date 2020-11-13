from PyQt5.QtCore import Qt, QUrl, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from views.QTBrowserWindow import Ui_BackgroundForm
from modules import StyleSheethHelper
from modules.BrowserTab import BrowserTab
import sys
import datetime
import sqlite3


class Wnd(QWidget, Ui_BackgroundForm):
    def __init__(self):
        super().__init__()
        self.is_pressed = False
        self.old_pos = QPoint(0, 0)

        self.setupUi(self)
        self.setWindowIcon(QIcon("./static/images/menu.png"))
        self.searchButton.clicked.connect(self.changeBrowserPage)
        self.webview.loadStarted.connect(self.loadStartedHook)
        self.webview.loadFinished.connect(self.loadFinishedHook)
        self.webview.urlChanged.connect(self.url_changet_hook)
        self.helloTab = BrowserTab(self, self.webview, self.tabsLayout)
        BrowserTab.chosenTab = self.helloTab
        self.helloTab.set_tab()

        self.btnReload.clicked.connect(self.webview.reload)
        self.btnGoBack.clicked.connect(self.goBack)
        self.btnGoForward.clicked.connect(self.goForward)

    def changeBrowserPage(self):
        try:
            self.webview.load(QUrl(self.searchField.text()))
        except Exception:
            self.webview.laod(QUrl("https://google.com"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = True
            self.old_pos = event.globalPos()

            if self.isMaximized():
                self.changeWindowState()

    def goBack(self):
        self.webview.page().history().back()

    def goForward(self):
        self.webview.page().history().forward()

    def mouseMoveEvent(self, event):
        if self.is_pressed:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_pressed = False

            if event.globalPos().y() == 0:
                self.changeWindowState()

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            self.changeBrowserPage()

    def changeWindowState(self):
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

    def loadStartedHook(self):
        self.btnReload.setIcon(QIcon("./static/images/close.png"))
        self.btnReload.setDisabled(True)

    def url_changet_hook(self):
        if self.webview.url().toString() == "about:blank":
            self.webview.load(QUrl("https://yandex.ru/search/?text=" + self.searchField.text()))
        else:
            if self.webview.url().url() != "https://ya.ru/":
                qtime = datetime.datetime.now().strftime("%H:%M:%S")
                qdate = datetime.datetime.now().strftime("%Y-%m-%d")
                qurl = self.webview.url().url()
                qtitle = self.webview.title()
                try:
                    db = sqlite3.connect("qtbrowser.db")
                    cur = db.cursor()
                    cur.execute(
                        f"""INSERT INTO history(title, url, date, time) VALUES ("{qtitle}", "{qurl}", "{qdate}", "{qtime}")""")
                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                self.historyWidget.add_item(qtitle, qurl, qtime, qdate)
            self.searchField.setText(self.webview.url().toString())

    def loadFinishedHook(self, ok):
        self.btnReload.setIcon(QIcon("./static/images/reload.png"))
        self.btnReload.setDisabled(False)


if __name__ == "__main__":
    app = QApplication([])
    wnd = Wnd()
    wnd.show()
    sys.exit(app.exec())
