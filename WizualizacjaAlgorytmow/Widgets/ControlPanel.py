from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Widgets.ControlPanelWidgets.ControlPanelButton import ControlPanelButton
from Widgets.ControlPanelWidgets.ControlPanelLabel import ControlPanelLabel
from Widgets.ControlPanelWidgets.ControlPanelTextBox import ControlPanelTextBox
from Widgets.ControlPanelWidgets.ControlPanelIconPanel import ControlPanelIconPanel

class ControlPanel(QWidget):
	"""
	Klasa reprezentująca panel kontrolny.

	Parametry:
	parent - widget rodzic.
	alignment - wyrównanie, domyślnie Qt.AlignTop
	"""
	def __init__(self, parent=None, alignment=Qt.AlignTop):
		super().__init__(parent)
		self.widgets = []
		self.widget_layout = None
		self.setup_ui(alignment)

	def setup_ui(self, alignment):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.widget_layout = QVBoxLayout(self)
		self.widget_layout.setContentsMargins(10, 10, 10, 10)
		self.widget_layout.setAlignment(alignment)
		self.widget_layout.setSpacing(4)
		self.setContentsMargins(0, 0, 0, 0)

	def clear(self):
		for widget in self.widgets:
			widget.setParent(None)
		self.widgets = []

	def add_icon_panel(self):
		icon_panel = ControlPanelIconPanel()
		self.widget_layout.addWidget(icon_panel)
		self.widgets.append(icon_panel)
		return icon_panel

	def add_button(self, text, icon_path=""):
		button = ControlPanelButton()
		button.set_icon(icon_path)
		button.set_text(text)
		self.widget_layout.addWidget(button)
		self.widgets.append(button)
		return button

	def add_label(self, text):
		label = ControlPanelLabel()
		label.setText(text)
		self.widget_layout.addWidget(label)
		self.widgets.append(label)

	def add_text_box(self):
		text_box = ControlPanelTextBox()
		self.widget_layout.addWidget(text_box)
		self.widgets.append(text_box)
		return text_box
