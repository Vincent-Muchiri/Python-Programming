import sys
from PySide6.QtWidgets import QApplication, QWidget

# TODO Create QApplication class
app = QApplication(sys.argv)

# TODO Create a window
window = QWidget()
window.show()

# QMainwindow is used to create menu bars, status bars etc
# QDialog is used to create dialog windows


# TODO Run the app
sys.exit(app.exec())
