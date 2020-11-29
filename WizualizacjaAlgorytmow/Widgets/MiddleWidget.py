from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Widgets.CenterWidget import CenterWidget
from Widgets.ControlPanel import ControlPanel

class MiddleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.widget_layout = QHBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)

        self.left_widget = CenterWidget(self)
        self.right_widget = ControlPanel(self)

        self.widget_layout.addWidget(self.left_widget, 4)
        self.widget_layout.addWidget(self.right_widget, 1)
        self.setLayout(self.widget_layout)
        pass