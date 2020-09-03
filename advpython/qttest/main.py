import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("Hi there!!! i am a label. Woot!")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        horizontal = QVBoxLayout()
        horizontal.addStretch(1)

        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()
        vertical.addWidget(label)
        vertical.addStretch(1)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)

        self.setWindowTitle("horizontal layout")
        self.show()


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