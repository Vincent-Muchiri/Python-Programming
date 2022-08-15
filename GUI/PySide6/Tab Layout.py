import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

app = QApplication(sys.argv)

tab = QTabWidget()
widget = QWidget()
layout = QGridLayout(widget) # What does this do?
tab.addTab(widget, "Tab 1")

tab.show()
app.exec()
