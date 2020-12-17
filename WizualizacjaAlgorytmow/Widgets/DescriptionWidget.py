from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class DescriptionWidget(QWebEngineView):
	"""
	Klasa reprezentująca centralny panel wyświetlający opis.

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
		pass

	def show_description(self, path):
		"""
		Wyświetla podany plik html jako opis.

		Parametry:
		path - ścieżka do pliku HTML.
		"""
		url = QUrl.fromLocalFile(path)
		self.load(url)
		self.show()