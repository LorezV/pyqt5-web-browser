from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import pyqtSlot, QUrl


class WebPage(QWebEnginePage):
    def __init__(self):
        super().__init__()

    def createWindow(self, _type):
        page = QWebEnginePage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @pyqtSlot(QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()
