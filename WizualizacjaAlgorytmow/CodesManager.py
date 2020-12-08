import random
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QDesktopServices
from Paths import Paths
from Algorithms.Algorithm import Algorithm

class CodesManager:
	"""
	Kontroler odpowiadający za obsługę implementacji.

	Parametry:
	main_widget - referencja do głównego widget'u.
	algorithm - obiekt algorytmu.
	"""
	def __init__(self, main_widget: QWidget, algorithm: Algorithm):
		self.algorithm = algorithm
		self.codes = self.algorithm.codes
		self.codes_buttons = []
		self.main_widget = main_widget
		self.control_panel_bottom = self.main_widget.middle_widget.right_widget.bottom_control_panel
		self.setup_control_panel()

	def setup_control_panel(self):
		"""
		Inicjalizuje panel kontrolny.
		"""
		self.codes_buttons = []
		for index, code in enumerate(self.codes):
			code_label = code.language.capitalize()
			if(code.language != "pseudocode"):
				code_label = "Kod " + code_label
			code_button = self.control_panel_bottom.add_button(code_label, code.icon)
			code_button.clicked.connect(lambda checked, index=index: self.on_click_code(index))
			code_button.set_hint("Wyświetlenie kodu źródłowego w przeglądarce.")
			self.codes_buttons.append(code_button)

	def on_click_code(self, index):
		"""
		Zdarzenie naciśnięcia przycisku.
		Uruchomienie kodu źródłowego algorytmu w przeglądarce.

		Parametry:
		index - numer wybranego kodu przez użytkownika
		"""
		QDesktopServices.openUrl(self.codes[index].url)