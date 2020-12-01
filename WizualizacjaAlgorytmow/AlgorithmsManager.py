from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QDesktopServices
from AlgorithmLoader import get_algorithm_list, Paths
from VisualisationManager import VisualisationManager
from QuestionsManager import QuestionsManager


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
		self.setup_algorithms()

	def setup_algorithms(self):
		"""
		Wczytuje algorytmy. 
		"""
		self.algorithms = get_algorithm_list()

		self.combobox.clear()
		for algorithm in self.algorithms:
			self.combobox.add_algorithms(algorithm.title, algorithm.difficulty)

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
		self.visualisation_button = self.control_panel_top.add_button("Wizualizacja", Paths.icon("eye.png"))
		self.visualisation_button.clicked.connect(self.show_visualisation)
		self.questions_button = self.control_panel_top.add_button("Pytania", Paths.icon("question_mark.png"))
		self.questions_button.clicked.connect(self.show_questions)

		self.codes_buttons = []
		for index, code in enumerate(self.current_algorithm.codes):
			code_button = self.control_panel_top.add_button(code.get_button_name(), code.icon)
			code_button.clicked.connect(self.on_click_code)
			code_button.set_hint("Wyświetlenie kodu źródłowego w przeglądarce.")
			self.codes_buttons.append(code_button)

	def on_click_code(self, index):
		"""
        Zdarzenie naciśnięcia przycisku.
        Uruchomienie kodu źródłowego algorytmu w przeglądarce.
        """
		QDesktopServices.openUrl(self.current_algorithm.codes[index].url)

	def on_change_algorithm(self, index):
		"""
        Zdarzenie zmiany algorytmu.
        Ustawia wybrany algorytm.
        """
		self.set_algorithm(index)
		pass

	def set_algorithm(self, index):
		"""
        Aktywuje dany algorytm.
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

	def reset(self):
		"""
		Przywraca stan programu do stanu początkowego.
        """
		self.setup_control_panel()
		self.manager = None
		self.show_description()
		pass
