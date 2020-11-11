from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from modules.BrowserTab import BrowserTab
import sqlite3


class HistoryWidget(QWidget):
    def __init__(self, widget, webview, container):
        super().__init__()
        self.setupUi()
        self.widget = widget
        self.webview = webview
        self.container = container

        self.listWidget = HistoryListWidget(self, self.widget, self.webview, self.container)
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.btnClearHistory)

        self.btnClearHistory.clicked.connect(self.clear_history)

        self.loadHistory()


    def setupUi(self):
        self.setMinimumSize(400, 600)
        self.setWindowTitle("История")
        self.setWindowIcon(QIcon("./static/images/reload.png"))
        self.btnClearHistory = QPushButton(self)
        self.btnClearHistory.setText("Отчистить историю")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

    def open(self):
        self.show()

    def clear_history(self):
        try:
            db = sqlite3.connect("qtbrowser.db")
            cur = db.cursor()
            cur.execute("DELETE FROM history")
            db.close()
        except Exception as e:
            print(e)

        while len(self.listWidget) != 0:
            self.listWidget.takeItem(0)


    def add_item(self, title, url, time, date):
        item = HistoryListItem(self.listWidget, url)
        # if (len(title) > )
        item.setText("\t".join([str(time)[:10] + ":", str(title)[:10], str(url)]))
        self.listWidget.addItem(item)
        del item

    def loadHistory(self):
        db = sqlite3.connect("qtbrowser.db")
        cur = db.cursor()
        historyData = cur.execute("""SELECT * FROM history""")
        historyData = list(map(lambda x: x, historyData))

        for x in historyData:
            self.add_item(x[1], x[2], x[4], x[3])

        db.close()


class HistoryListWidget(QListWidget):
    def __init__(self, parent, widget,  webview, container):
        super().__init__(parent)
        self.widget = widget
        self.webview = webview
        self.container = container

        self.itemClicked.connect(self.item_clicked_hook)

    def item_clicked_hook(self, item):
        try:
            tab = BrowserTab(self.widget, self.webview, self.container)
            tab.webpage.load(QUrl(item.url()))
            tab.set_tab()
        except Exception as e:
            print(e)


class HistoryListItem(QListWidgetItem):
    def __init__(self, parent, url):
        super().__init__(parent)
        self.__url = url

    def url(self):
        return self.__url
