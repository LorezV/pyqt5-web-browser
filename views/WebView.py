from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl


class WebView(QWebEngineView):
    def __init__(self, Form):
        super().__init__()
        self.form = Form
        self.setupUi()
        self.url = QUrl("https://vk.com/")


        self.webview.load(self.url)

    def setupUi(self):
        self.webview = QWebEngineView(self.form)
        self.webview.setObjectName("webview")
        self.webview.show()
