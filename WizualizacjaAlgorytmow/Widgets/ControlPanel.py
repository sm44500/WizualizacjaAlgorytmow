from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Widgets.ControlPanelButton import ControlPanelButton

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.buttons = []
        self.setup_ui()

    def setup_ui(self):
        self.setMaximumWidth(300)
        self.setMinimumWidth(200)
        self.setStyleSheet("""
            background-color: red;
        """)

        self.widget_layout = QVBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignTop)

    def clear(self):
        for button in self.buttons:
            button.setParent(None)
        self.buttons = []

    def add_button(self, text, icon_path=""):
        button = ControlPanelButton()
        button.set_icon(icon_path)
        button.set_text(text)
        self.widget_layout.addWidget(button)
        self.buttons.append(button)
        return button