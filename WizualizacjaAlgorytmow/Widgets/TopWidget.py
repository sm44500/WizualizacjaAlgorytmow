from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Paths import *


class TopWidget(QComboBox):
	"""
	Klasa reprezentująca górny panel.
	Lista rozwijana.

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

	def add_algorithms(self, algorithm_name):
		"""
		Dodaje algorytm do listy rozwijanej.

		Parametry:
		algorithm_name - tytuł algorytmu do dodania.
		"""
		self.addItem(algorithm_name)

	def set_difficulty(self, index, difficulty):
		"""
		Ustawia ikonę symbolizującą poziom trudności algorytmu do listy rozwijanej.

		Parametry:
		index - numer pozycji w liście rozwijanej
		difficulty - poziom trudności
		"""
		self.setItemIcon(index, QIcon(Paths.icon("difficulty_"+str(difficulty)+".png")))