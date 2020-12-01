from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Widgets.ControlPanel import ControlPanel

class RightPanel(QWidget):
	"""
	Klasa reprezentująca prawy panel.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setMaximumWidth(300)
		self.setMinimumWidth(200)
		self.widget_layout = QVBoxLayout(self)
		self.widget_layout.setContentsMargins(0, 4, 0, 4)

		self.top_control_panel = ControlPanel(self, Qt.AlignTop)
		self.bottom_control_panel = ControlPanel(self, Qt.AlignBottom)
		
		self.widget_layout.addWidget(self.top_control_panel)
		self.widget_layout.addWidget(self.bottom_control_panel)
		self.setLayout(self.widget_layout)