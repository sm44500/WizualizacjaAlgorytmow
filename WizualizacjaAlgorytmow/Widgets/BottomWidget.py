from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class BottomWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setMaximumHeight(300)
        self.setMinimumHeight(200)
        self.setStyleSheet("""
            background-color: red;
        """)
        pass

    def set_text(self, content: str):
        self.setText(content)
