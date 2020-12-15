from PyQt5.QtWidgets import QWidget
from VisualisationManager import VisualisationManager
from QuestionsManager import QuestionsManager
from CodesManager import CodesManager
from Paths import Paths

import Algorithms

class AlgorithmsManager:
	"""
	Kontroler odpowiadający za obsługę algorytmu.

	Parametry:
	main_widget - referencja do głównego widget'u.
	"""
	def __init__(self, main_widget: QWidget):
		self.algorithms = []
		self.main_widget = main_widget
		self.combobox = self.main_widget.top_widget
		self.control_panel_top = self.main_widget.middle_widget.right_widget.top_control_panel
		self.control_panel_bottom = self.main_widget.middle_widget.right_widget.bottom_control_panel
		self.center = self.main_widget.middle_widget.left_widget
		self.bottom = self.main_widget.bottom_widget
		self.manager = None
		self.current_index = 0
		self.current_algorithm = None
		self.description_button = None
		self.visualisation_button = None
		self.questions_button = None
		self.codes_button = None
		self.setup_algorithms()

	def setup_algorithms(self):
		"""
		Wczytuje algorytmy. 
		"""
		self.algorithms = []

		self.combobox.clear()
		for algorithm_class in Algorithms.AlgorythmsClasses:
			algorithm = algorithm_class()
			self.combobox.add_algorithms(algorithm.title, algorithm.difficulty)
			self.algorithms.append(algorithm)

		self.main_widget.top_widget.currentIndexChanged.connect(self.on_change_algorithm)

		self.set_algorithm(0)

	def setup_control_panel(self):
		"""
		Inicjalizuje panel kontrolny.
		"""
		self.control_panel_top.clear()
		self.control_panel_bottom.clear()

		self.description_button = self.control_panel_top.add_button("Opis", Paths.icon("bookmark.png"))
		self.description_button.clicked.connect(self.show_description)
		self.description_button.set_hint("Wyświetlenie opisu algorytmu.")

		self.visualisation_button = self.control_panel_top.add_button("Wizualizacja", Paths.icon("eye.png"))
		self.visualisation_button.clicked.connect(self.show_visualisation)
		self.visualisation_button.set_hint("Wizualizacja podstawowych operacji na rzecz danego algorytmu.")

		self.codes_button = self.control_panel_top.add_button("Kody źródłowe", Paths.icon("code.png"))
		self.codes_button.clicked.connect(self.show_codes)
		self.codes_button.set_hint("Przejście do panelu z kodami źródłowymi.")

		self.questions_button = self.control_panel_top.add_button("Pytania", Paths.icon("question_mark.png"))
		self.questions_button.clicked.connect(self.show_questions)
		self.questions_button.set_hint("Panel weryfikujący zdobytą przez użytkownika wiedzę.")

	def on_change_algorithm(self, index):
		"""
		Zdarzenie zmiany algorytmu.
		Ustawia wybrany algorytm.

		Parametry:
		index - numer algorytmu.
		"""
		self.set_algorithm(index)
		pass

	def set_algorithm(self, index):
		"""
		Aktywuje dany algorytm.

		Parametry:
		index - numer algorytmu.
		"""
		self.current_index = index
		self.current_algorithm = self.algorithms[index]
		self.reset()

	def show_description(self):
		"""
		Wyświetla opis algorytmu 
		"""
		self.center.clear_widget()
		self.setup_control_panel()
		self.manager = None
		self.bottom.set_text(self.current_algorithm.description)

	def show_visualisation(self):
		"""
		Uruchamia zarządcę odpowiedzialnego za wizualizacje algorytmu.
		"""
		self.center.clear_widget()
		self.setup_control_panel()
		self.manager = VisualisationManager(self.main_widget, self.current_algorithm)

	def show_questions(self):
		"""
		Uruchamia zarządcę odpowiedzialnego za pytania testowe.
		"""
		if len(self.current_algorithm.test_questions) > 0:
			self.center.clear_widget()
			self.setup_control_panel()
			self.manager = QuestionsManager(self.main_widget, self.current_algorithm)

	def show_codes(self):
		"""
		Uruchamia zarządcę odpowiedzialnego za wyświetlanie implementacji.
		"""
		if len(self.current_algorithm.codes) > 0:
			self.center.clear_widget()
			self.setup_control_panel()
			self.manager = CodesManager(self.main_widget, self.current_algorithm)

	def reset(self):
		"""
		Przywraca stan programu do stanu początkowego.
		"""
		self.setup_control_panel()
		self.manager = None
		self.show_description()
		pass
