from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebWidget(QWebEngineView):
	"""
	Klasa reprezentująca panel przeglądarki web.

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

	def show_html_file(self, path):
		"""
		Wyświetla podany plik html.

		Parametry:
			path - ścieżka do pliku HTML.
		"""
		url = QUrl.fromLocalFile(path)
		self.load(url)
		self.show()