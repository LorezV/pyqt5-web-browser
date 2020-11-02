from PyQt5 import Qt
import syntax_2

app = Qt.QApplication([])
editor = Qt.QPlainTextEdit()


font = Qt.QFont()
font.setPointSize(12)
editor.setFont(font)

highlight = syntax_2.PythonHighlighter(editor.document())
editor.show()
editor.resize(700, 400)

# Загрузите что-нибудь (например, editor_2.py) в редактор для демонстрации.
infile = open('editor_2.py', 'r')
editor.setPlainText(infile.read())

app.exec_()
