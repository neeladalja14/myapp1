import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked Me!: 0")
        self.button.pressed.connect(self.pressButton)
        self.button.released.connect(self.clickedButton)

        h = QHBoxLayout()
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        v.addLayout(h)
        v.addWidget(self.button)


        self.setLayout(v)

        self.setWindowTitle("Horizontal Layout")
        self.show()


    def clickedButton(self):
        print("This is button, has been released")


    def pressButton(self):
        print("This is being pressed")
        self.counter += 1
        self.button.setText("Clicked: " + str(self.counter))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())






"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)

        my_label = QLabel("this is my label")
        layout = QVBoxLayout()

        layout.addWidget(my_label)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("my first layout")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec_())
"""