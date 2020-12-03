from PyQt5.QtWidgets import QSlider


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
		pass
