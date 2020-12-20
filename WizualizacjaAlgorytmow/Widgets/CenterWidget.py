from PyQt5.QtWidgets import QHBoxLayout

from Styles import Styles
from Widgets.BaseWidget import BaseWidget


class CenterWidget(BaseWidget):
	"""
	Klasa reprezentująca centralny panel aplikacji.

	Parametry:
		parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QHBoxLayout)
		self.widget = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setStyleSheet(Styles.description_background)

	def clear_widget(self):
		"""
		Czyszczenie widget'u z odepnięciem go od rodzica wpierw.
		"""
		if self.widget is not None:
			self.widget.setParent(None)
			self.widget = None

	def set_widget(self, widget_class):
		"""
		Tworzy widget o podanej klasie i ustawia na sobie.

		Parametry:
			widget_class - Typ klasy widget'u
		"""
		self.widget = widget_class()
		self.widget_layout.addWidget(self.widget)
