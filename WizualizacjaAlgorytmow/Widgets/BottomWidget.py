from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class BottomWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        font = QFont()
        self.setStyleSheet("""
            background-color: #bcbcbc;
            padding: 10px;
        """)
        font.setPointSize(20)
        font.setBold(True)
        self.setFont(font)
        self.setMaximumHeight(300)
        self.setMinimumHeight(200)
        pass

    def set_text(self, content: str):
        self.setText(content)
        self.setWordWrap(True)
