formFormStyleSheet_normal = ("QWidget {\n"
                             "background-color: #2C2C3B;\n"
                             "border-top-left-radius: 15px; \n"
                             "border-top-right-radius: 15px; \n"
                             "color: white;"
                             "}")
formFormStyleSheet_maximized = ("QWidget {\n"
                                "background-color: #2C2C3B;\n"
                                "border-radius: 0px; \n"
                                "}")

btnQtMenuStyleSheet_normal = ("QMenuBar {\n"
                              "background-color: #40CD52;\n"
                              "color: white;\n"
                              "border: none;\n"
                              "padding-left: 10px;"
                              "border-radius: 0px;\n"
                              "border-top-left-radius: 15px;\n"
                              "}"
                              "QMenu {"
                              "background-color: #40CD52;"
                              "color: white;"
                              "border: 1px solid white;"
                              "border-radius: none;"
                              "}"
                              "QMenuBar::item {"
                              "background-color: rgba(0, 0, 0, 0);"
                              "margin-left: 25px;"
                              "margin-top: 5px;"
                              "}")

btnQtMenuStyleSheet_maximized = btnQtMenuStyleSheet_normal + ("QMenuBar {\n"
                                 "border: none;\n"
                                 "border-radius: 0px;\n"
                                 "}")

btnMinimizeStyleSheet_normal = ("QPushButton {\n"
                                "border: none;\n"
                                "color: white;\n"
                                "background-color: #F1B30F;\n"
                                "border-radius: 7px;\n"
                                "}")

btnMaximizeStyleSheet_normal = ("QPushButton {\n"
                                "border: none;\n"
                                "color: white;\n"
                                "border-radius: 7px;\n"
                                "background-color: #35B132;\n"
                                "}")

btnCloseStyleSheet_normal = ("QPushButton {\n"
                             "border: none;\n"
                             "color: white;\n"
                             "background-color: #E35F50;\n"
                             "border-radius: 7px;\n"
                             "}")
searchFieldStyleSheet_normal = ("QLineEdit { \n"
                                "background-color: white;\n"
                                "color: black; \n"
                                "border-radius: 0px;"
                                "border-bottom: 1px solid gray;"
                                "}")
actionButtonStyleSheet_normal = ("QPushButton {"
                                 "border-radius: 0px;"
                                 "} \n"
                                 "QPushButton:hover {"
                                 "background-color: #636e72;"
                                 "}")
browserTabStyleSheet = ("QPushButton {"
                        "border-radius: 0px;"
                        "background-color: #ecf0f1;"
                        "text-align: left;"
                        "color: black;"
                        "font-size: 14px;"
                        "padding: 0px 5px 0px 5px"
                        "}")
browserTabStyleSheet_chosen = browserTabStyleSheet + ("QPushButton {"
                                                      "background-color: #c8d6e5;"
                                                      "}")
browserCloseTabStyleSheet = ("QPushButton {"
                             "border-right: 1px solid gray;"
                             "image: url('./static/images/close_black.png');"
                             "}"
                             "QPushButton:hover {"
                             "background-color: #e74c3c;"
                             "image: url('./static/images/close.png');"
                             "}")
