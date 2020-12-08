from PyQt5.QtWidgets import QSlider

from Styles import Styles


class ControlPanelSlider(QSlider):
	"""
	Klasa reprezentująca suwak.

	Parametry:
	parent - rodzic, do którego zostanie podłączony ten widget.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.init_ui()

	def init_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setMinimumHeight(20)
		self.setStyleSheet(Styles.slider_background)
