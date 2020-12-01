from PyQt5.QtWidgets import QWidget, QVBoxLayout

from Widgets.TopWidget import TopWidget
from Widgets.MiddleWidget import MiddleWidget
from Widgets.BottomWidget import BottomWidget
from Widgets.BaseWidget import BaseWidget


class MainWidget(BaseWidget):
	"""
	Głowna klasa reprezentująca wygląd aplikacji.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QVBoxLayout)
		self.top_widget = None
		self.middle_widget = None
		self.bottom_widget = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.widget_layout.setContentsMargins(5, 5, 5, 5)
		
		self.top_widget = TopWidget(self)
		self.middle_widget = MiddleWidget(self)
		self.bottom_widget = BottomWidget(self)

		self.widget_layout.addWidget(self.top_widget, 1)
		self.widget_layout.addWidget(self.middle_widget, 80)
		self.widget_layout.addWidget(self.bottom_widget, 20)
