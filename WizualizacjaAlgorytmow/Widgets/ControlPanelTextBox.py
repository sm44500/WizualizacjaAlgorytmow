from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ControlPanelTextBox(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        font = QFont()
        self.setStyleSheet("""
            background-color: red;
        """)
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setMinimumHeight(40)