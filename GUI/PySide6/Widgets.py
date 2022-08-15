from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QSlider, QTabWidget, QGridLayout
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtCore import QSize, QCoreApplication, Qt
import sys


# TODO Create the Window class
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 500, 700)
        self.setWindowTitle("PySide GUI Widgets")
        self.setWindowIcon(QIcon("images/python_icon.png"))
        self.setStyleSheet("background-color:white")
        self.setWindowOpacity(0.9)

        # TODO Create a text label
        text_label = QLabel("Hello World", self)
        # label.setText("This is PySide6")
        text_label.setFont(QFont("Ariel", 24))
        text_label.setStyleSheet("color:red")
        
        # TODO Create an image label
        pic_label = QLabel(self)
        img = QPixmap("images/python_icon.png")
        pic_label.setPixmap(img)
        pic_label.move(200, 0)

        # TODO Create button widget with text
        text_btn = QPushButton("Click", self)
        text_btn.setText("Call Function")
        text_btn.setGeometry(0, 50, 80, 50)
        text_btn.setFont(QFont("Calibre", 8))

        # TODO Run a function when the button is clicked
        def clickme():
            print("I was clicked")
        text_btn.clicked.connect(clickme)


        # TODO Create image button
        img_btn = QPushButton("Python", self)
        img_btn.setGeometry(100, 50, 100, 50)
        img_btn.setIcon(QIcon("images/python_icon.png"))
        img_btn.setIconSize(QSize(96, 96))
        img_btn.setStyleSheet("background-color:grey")

        # TODO Button to exit the app
        exit_btn = QPushButton("Exit", self)
        exit_btn.setGeometry(210, 50, 50, 30)
        exit_btn.clicked.connect(QCoreApplication.instance().quit)

        # TODO Create text edit
        text_edit = QTextEdit()
        text_edit.setGeometry(0, 200, 50, 20)

        # TODO Create a horizontal slider
        # hor_slider = QSlider(Qt.Horizontal)
        # hor_slider.setGeometry(0, 250, 100, 100)

        # TODO Create tabs
        tab = QTabWidget()
        widget = QWidget()
        layout = QGridLayout(widget)
        tab.addTab(widget, "Tab 1")


# Create the app object
app = QApplication(sys.argv)

# TODO Create the window object
window = Window()
window.show()

# TODO Execute the app
sys.exit(app.exec())

