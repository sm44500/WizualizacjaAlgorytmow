from PyQt5.QtWidgets import QWidget, QHBoxLayout

from Widgets.CenterWidget import CenterWidget
from Widgets.RightPanel import RightPanel
from Widgets.BaseWidget import BaseWidget


class MiddleWidget(BaseWidget):
	"""
	Klasa reprezentująca środkowy panel.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QHBoxLayout)
		self.left_widget = None
		self.right_widget = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.left_widget = CenterWidget(self)
		self.right_widget = RightPanel(self)

		self.widget_layout.addWidget(self.left_widget, 6)
		self.widget_layout.addWidget(self.right_widget, 1)
