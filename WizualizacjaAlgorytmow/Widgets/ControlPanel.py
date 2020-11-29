from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Widgets.ControlPanelButton import ControlPanelButton
from Widgets.ControlPanelLabel import ControlPanelLabel
from Widgets.ControlPanelTextBox import ControlPanelTextBox


class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widgets = list()
        self.widget_layout = None
        self.setup_ui()

    def setup_ui(self):
        self.setMaximumWidth(300)
        self.setMinimumWidth(200)

        self.widget_layout = QVBoxLayout(self)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignTop)
        self.widget_layout.setSpacing(0)

        self.setContentsMargins(0, 0, 0, 0)

    def clear(self):
        for widget in self.widgets:
            widget.setParent(None)
        self.widgets = list()

    def add_button(self, text, icon_path=""):
        button = ControlPanelButton()
        button.set_icon(icon_path)
        button.set_text(text)
        self.widget_layout.addWidget(button)
        self.widgets.append(button)
        return button

    def add_text_box(self, hint="Wartość elementu:"):
        label = ControlPanelLabel()
        label.setText(hint)
        self.widget_layout.addWidget(label)
        self.widgets.append(label)

        text_box = ControlPanelTextBox()
        self.widget_layout.addWidget(text_box)
        self.widgets.append(text_box)

        return label, text_box
