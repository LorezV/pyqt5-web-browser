from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from modules import StyleSheethHelper
import pytube

class DownloadButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi()
        self._parent = parent

        parent.webview.urlChanged.connect(self.url_changed)
        self.clicked.connect(self.request_download)

    def setupUi(self):
        self.setIcon(QIcon("./static/images/download.svg"))
        self.setFixedSize(QSize(30, 30))
        self.setIconSize(QSize(15, 15))
        self.setStyleSheet(StyleSheethHelper.actionButtonStyleSheet_normal)
        self.hide()

    def url_changed(self):
            if "https://www.youtube.com/watch?" in self._parent.webview.url().url():
                self.show()
            else:
                self.hide()

    def request_download(self):
        try:
            yt = pytube.YouTube(self._parent.webview.url().url())
            videos = yt.streams\
                .filter(progressive=True, file_extension="mp4")\
                .order_by('resolution')\
                .desc()\
                .first()\
                .download("./videos")
        except Exception as e:
            print(e)