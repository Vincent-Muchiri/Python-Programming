from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
import sys

# TODO Create a master class to enable us to use the attributes
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # TODO Set the geometry
        self.setGeometry(710, 290, 500, 500)
        self.setWindowTitle("PySide GUI Window")
        self.setWindowIcon(QIcon("images/python_icon.png"))
        self.setStyleSheet('background-color:grey')
        self.setWindowOpacity(0.5) # Takes a value between 0 and 1

app = QApplication(sys.argv)
window = Window()
window.show()

# TODO Run the app
sys.exit(app.exec())
