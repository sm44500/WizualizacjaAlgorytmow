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
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.widget_layout)
        self.setStyleSheet("""
            background-color: grey;
        """)
        pass

    def clear_widget(self):
        if not self.widget is None:
            self.widget.setParent(None)
            self.widget = None

    def set_widget(self, widget_class, snapshot, description_widget):
        self.widget = widget_class(snapshot, description_widget)
        self.widget_layout.addWidget(self.widget)

    def set_visualisation_widget(self, widget_class, snapshot, description_widget):
        self.widget = widget_class(snapshot, description_widget)
        self.widget_layout.addWidget(self.widget)
