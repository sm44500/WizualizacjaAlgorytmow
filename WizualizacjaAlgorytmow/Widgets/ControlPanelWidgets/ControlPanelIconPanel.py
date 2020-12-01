from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from Widgets.ControlPanelWidgets.ControlPanelIconPanelButton import ControlPanelIconPanelButton

class ControlPanelIconPanel(QWidget):
	"""
	Kontrolka panelu kontrolnego. Panel z ikonami.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.widgets = []
		self.widget_layout = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.widget_layout = QHBoxLayout(self)
		self.widget_layout.setContentsMargins(0, 10+10, 0, 10)
		self.widget_layout.setAlignment(Qt.AlignHCenter)
		self.widget_layout.setSpacing(0)
		self.setContentsMargins(0, 0, 0, 0)
	
	def clear(self):
		for widget in self.widgets:
			widget.setParent(None)
		self.widgets = []

	def add_button(self, icon_path="", hint=""):
		button = ControlPanelIconPanelButton()
		button.set_icon(icon_path)
		button.set_hint(hint)
		self.widget_layout.addWidget(button)
		self.widgets.append(button)

		return button
