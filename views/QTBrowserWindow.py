from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_BackgroundForm(object):
    def setupUi(self, BackgroundForm):
        BackgroundForm.setWindowFlags(Qt.CustomizeWindowHint)
        BackgroundForm.setObjectName("BackgroundForm")
        BackgroundForm.resize(1074, 782)
        BackgroundForm.setMouseTracking(True)
        self.gridLayout_3 = QGridLayout(BackgroundForm)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Form = QWidget(BackgroundForm)
        self.Form.setMouseTracking(False)
        self.Form.setStyleSheet("QWidget {\n"
                                "background-color: white;\n"
                                "}")
        self.Form.setObjectName("Form")
        self.gridLayout_2 = QGridLayout(self.Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName("headerLayout")
        self.btnQtMenu = QPushButton(self.Form)
        self.btnQtMenu.setMinimumSize(QSize(150, 30))
        self.btnQtMenu.setMaximumSize(QSize(150, 30))
        id = QFontDatabase.addApplicationFont("./static/fonts/Montserrat-Regular.ttf")
        font = QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnQtMenu.setFont(font)
        self.btnQtMenu.setStyleSheet("QPushButton {\n"
                                     "background-color: #40CD52;\n"
                                     "color: white;\n"
                                     "border: none;\n"
                                     "border-radius: 0px;\n"
                                     "border-top-left-radius: 15px;\n"
                                     "border-bottom-right-radius: 15px;\n"
                                     "}")
        self.btnQtMenu.setIcon(QIcon("./static/images/menu.png"))
        self.btnQtMenu.setObjectName("btnQtMenu")
        self.headerLayout.addWidget(self.btnQtMenu)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        self.closeMinMaxLayout = QHBoxLayout()
        self.closeMinMaxLayout.setContentsMargins(5, 0, 5, -1)
        self.closeMinMaxLayout.setSpacing(10)
        self.closeMinMaxLayout.setObjectName("closeMinMaxLayout")
        self.btnMinimize = QPushButton(self.Form)
        self.btnMinimize.setMinimumSize(QSize(15, 15))
        self.btnMinimize.setMaximumSize(QSize(15, 15))
        self.btnMinimize.setStyleSheet("QPushButton {\n"
                                       "border: none;\n"
                                       "color: white;\n"
                                       "background-color: #BABABA;\n"
                                       "border-radius: 7px;\n"
                                       "}")
        self.btnMinimize.setText("")
        self.btnMinimize.setObjectName("btnMinimize")
        self.closeMinMaxLayout.addWidget(self.btnMinimize)
        self.btnMaximize = QPushButton(self.Form)
        self.btnMaximize.setMinimumSize(QSize(15, 15))
        self.btnMaximize.setMaximumSize(QSize(15, 15))
        self.btnMaximize.setStyleSheet("QPushButton {\n"
                                       "border: none;\n"
                                       "color: white;\n"
                                       "border-radius: 7px;\n"
                                       "background-color: #BABABA;\n"
                                       "}")
        self.btnMaximize.setText("")
        self.btnMaximize.setObjectName("btnMaximize")
        self.closeMinMaxLayout.addWidget(self.btnMaximize)
        self.btnClose = QPushButton(self.Form)
        self.btnClose.setMinimumSize(QSize(15, 15))
        self.btnClose.setMaximumSize(QSize(15, 15))
        self.btnClose.setAccessibleDescription("")
        self.btnClose.setStyleSheet("QPushButton {\n"
                                    "border: none;\n"
                                    "color: white;\n"
                                    "background-color: #e74c3c;\n"
                                    "border-radius: 7px;\n"
                                    "}")
        self.btnClose.setText("")
        self.btnClose.setObjectName("btnClose")
        self.closeMinMaxLayout.addWidget(self.btnClose)
        self.headerLayout.addLayout(self.closeMinMaxLayout)
        self.gridLayout_2.addLayout(self.headerLayout, 0, 0, 1, 1)
        self.plainTextEdit = QPlainTextEdit(self.Form)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit\n"
                                         "{\n"
                                         "background-color: #F0F5F8;\n"
                                         "outline: none;\n"
                                         "border-radius: 0px;\n"
                                         "}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFont(QFont("Montserrat", 12))
        self.gridLayout_2.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Form, 0, 0, 1, 1)

        self.retranslateUi(BackgroundForm)
        QMetaObject.connectSlotsByName(BackgroundForm)

    def retranslateUi(self, BackgroundForm):
        _translate = QCoreApplication.translate
        BackgroundForm.setWindowTitle(_translate("BackgroundForm", "QtCodeEditor"))
        self.btnQtMenu.setText(_translate("BackgroundForm", "QtCodeEditor"))
