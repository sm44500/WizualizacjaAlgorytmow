from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ControlPanelButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        buttons = []
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

    def set_icon(self, icon_path):
        icon = QIcon(icon_path)
        self.setIcon(icon)
        self.setIconSize(QSize(32, 32))

    def set_text(self, text):
        self.setText(text)