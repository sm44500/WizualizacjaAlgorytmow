from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CenterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widget = None
        self.setup_ui()

    def setup_ui(self):
        self.widget_layout = QHBoxLayout(self)
        self.setLayout(self.widget_layout)
        self.setStyleSheet("""
            background-color: red;
        """)
        pass

    def clear_widget(self):
        if not self.widget is None:
            self.widget.setParent(None)
            self.widget = None

    def set_widget(self, widget_class):
        self.widget = widget_class(self)
        self.widget_layout.addWidget(self.widget)