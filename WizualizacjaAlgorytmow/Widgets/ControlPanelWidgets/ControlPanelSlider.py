from PyQt5.QtWidgets import QSlider

from Styles import Styles


class ControlPanelSlider(QSlider):
	"""
	Klasa reprezentująca suwak.

	Parametry:
		parent - rodzic, do którego zostanie podłączony ten widget.
	"""
	def __init__(self, value, parent=None):
		super().__init__(parent)
		self.init_ui()
		self.value_to_update = value
		self.setValue(value[0])

	def init_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setMinimumHeight(20)
		self.setStyleSheet(Styles.slider_background)
		self.valueChanged.connect(self.update_value)

	def update_value(self):
		"""
		Aktualizacja wartości przy każdym przesunięciu suwaka.
		"""
		self.value_to_update[0] = self.value()
