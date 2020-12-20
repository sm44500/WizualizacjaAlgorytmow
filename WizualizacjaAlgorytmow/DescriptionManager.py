import random
from PyQt5.QtWidgets import QWidget, QMessageBox
from Paths import Paths
from AlgorithmsLogic import Algorithm
from Widgets.WebWidget import WebWidget

class DescriptionManager:
	"""
	Kontroler odpowiadający za obsługę wyświetlania opisu.

	Parametry:
		main_widget - referencja do głównego widget'u.
		algorithm - obiekt algorytmu.
	"""
	def __init__(self, main_widget: QWidget, algorithm: Algorithm):
		self.algorithm = algorithm
		self.main_widget = main_widget
		self.center = self.main_widget.middle_widget.left_widget
		self.setup_center_panel()
		self.current_question_index = 0

	def setup_center_panel(self):
		"""
		Inicjalizuje panel centralny z opisem.
		"""
		self.center.set_widget(WebWidget)
		self.center.widget.show_html_file(Paths.description(self.algorithm.name))

	
