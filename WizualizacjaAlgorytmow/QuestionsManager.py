from PyQt5.QtWidgets import QWidget
from Paths import Paths
from Algorithms.Algorithm import Algorithm

class QuestionsManager:
	"""
	Kontroler odpowiadający za obsługę pytań.

	Parametry:
	main_widget - referencja do głównego widget'u.
	algorithm - obiekt algorytmu.
	"""
	def __init__(self, main_widget: QWidget, algorithm: Algorithm):
		self.algorithm = algorithm
		self.main_widget = main_widget
		self.control_panel_bottom = self.main_widget.middle_widget.right_widget.bottom_control_panel
		self.center = self.main_widget.middle_widget.left_widget
		self.description_widget = self.main_widget.bottom_widget
		self.answer_buttons = []
		self.answers = [-1] * len(self.algorithm.test_questions)
		self.setup_control_panel()
		self.current_question_index = 0
		self.is_playing = False

	def setup_control_panel(self):
		"""
		Inicjalizuje panel kontrolny.
		"""
		self.title_label = self.control_panel_bottom.add_label("Odpowiedź:")
		self.icon_panel = self.control_panel_bottom.add_icon_panel()

		self.previous_button = self.icon_panel.add_button(Paths.icon("backward.png"), "Poprzednie pytanie")
		self.previous_button.clicked.connect(self.on_click_previous)

		answer_button = self.icon_panel.add_button(Paths.icon("letter_a.png"), "Odpowiedź A")
		answer_button.clicked.connect(lambda: self.on_click_answer(0))
		self.answer_buttons.append(answer_button)

		answer_button = self.icon_panel.add_button(Paths.icon("letter_b.png"), "Odpowiedź B")
		answer_button.clicked.connect(lambda: self.on_click_answer(1))
		self.answer_buttons.append(answer_button)

		answer_button = self.icon_panel.add_button(Paths.icon("letter_c.png"), "Odpowiedź C")
		answer_button.clicked.connect(lambda: self.on_click_answer(2))
		self.answer_buttons.append(answer_button)

		answer_button = self.icon_panel.add_button(Paths.icon("letter_d.png"), "Odpowiedź D")
		answer_button.clicked.connect(lambda: self.on_click_answer(3))
		self.answer_buttons.append(answer_button)

		self.next_button = self.icon_panel.add_button(Paths.icon("forward.png"), "Następne pytanie")
		self.next_button.clicked.connect(self.on_click_next)

	def on_click_previous(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Zmienia pytanie na poprzednie.
		"""
		question = self.previous_question()
		self.description_widget.show_question(question)	

	def on_click_next(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Zmienia pytanie na następne.
		"""
		question = self.next_question()
		self.description_widget.show_question(question)	

	def on_click_answer(self, answer: int):
		"""
		Zdarzenie naciśnięcia przycisku odpowiedzi.
		Ustawia wybraną odpowiedz.

		Parametry:
		answer - numer odpowiedzi
		"""
		print(answer)

	def next_question(self):
		"""
		Zmienia pytanie na następne.
		"""
		self.current_question_index = max(0, min(len(self.algorithm.test_questions) - 1, self.current_question_index + 1))
		return self.algorithm.test_questions[self.current_question_index]

	def previous_question(self):
		"""
		Zmienia pytanie na następne.
		Zmienia pytanie na poprzednie.
		"""
		self.current_question_index = max(0, self.current_question_index - 1)
		return self.algorithm.test_questions[self.current_question_index]