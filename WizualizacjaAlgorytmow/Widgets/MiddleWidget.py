from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Styles import Styles
from Widgets.CenterWidget import CenterWidget
from Widgets.RightPanel import RightPanel

class MiddleWidget(QWidget):
	"""
	Klasa reprezentująca środkowy panel.

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
		self.widget_layout = QHBoxLayout(self)
		self.widget_layout.setContentsMargins(0, 0, 0, 0)
		self.widget_layout.setSpacing(0)

		self.left_widget = CenterWidget(self)
		self.right_widget = RightPanel(self)

		self.widget_layout.addWidget(self.left_widget, 6)
		self.widget_layout.addWidget(self.right_widget, 1)
		self.setLayout(self.widget_layout)
