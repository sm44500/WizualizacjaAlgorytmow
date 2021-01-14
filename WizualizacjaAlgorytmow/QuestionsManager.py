import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox
from Paths import Paths
from Styles import Styles
from TestScoreWindow import TestScoreWindow
from Widgets.QuestionsWidget import QuestionsWidget
from AlgorithmsLogic import Algorithm

class QuestionsManager:
	"""
	Kontroler odpowiadający za obsługę pytań.

	Parametry:
		main_widget - referencja do głównego widget'u.

		algorithm - obiekt algorytmu.
	"""
	def __init__(self, main_widget: QWidget, algorithm: Algorithm):
		self.algorithm = algorithm
		self.questions = self.algorithm.test_questions[:]
		self.main_widget = main_widget
		self.control_panel_bottom = self.main_widget.middle_widget.right_widget.bottom_control_panel
		self.center = self.main_widget.middle_widget.left_widget
		self.questions_widget = None
		self.answers = [-1] * len(self.questions)
		self.is_end = False
		self.setup_ui()
		self.current_question_index = 0
		random.shuffle(self.questions)
		self.set_question(self.questions[self.current_question_index])

	def setup_ui(self):
		"""
		Inicjalizuje interfejs użytkownika.
		"""

		self.center.set_widget(QuestionsWidget)
		self.questions_widget = self.center.widget

		self.check_button = self.control_panel_bottom.add_button("Zakończ test", Paths.icon("eye.png"), "Sprawdza test")
		self.check_button.clicked.connect(self.on_click_check)

		for index, answer_button in enumerate(self.questions_widget.answers):
			answer_button.clicked.connect((lambda i: lambda: self.on_click_answer(i))(index))

		self.control_icon_panel = self.control_panel_bottom.add_icon_panel()

		self.first_button = self.control_icon_panel.add_button(Paths.icon("first.png"), "Pierwsze pytanie")
		self.first_button.clicked.connect(self.on_click_first)

		self.previous_button = self.control_icon_panel.add_button(Paths.icon("backward.png"), "Poprzednie pytanie")
		self.previous_button.clicked.connect(self.on_click_previous)

		self.next_button = self.control_icon_panel.add_button(Paths.icon("forward.png"), "Następne pytanie")
		self.next_button.clicked.connect(self.on_click_next)

		self.last_button = self.control_icon_panel.add_button(Paths.icon("last.png"), "Ostatnie pytanie")
		self.last_button.clicked.connect(self.on_click_last)

	def on_click_previous(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Zmienia pytanie na poprzednie.
		"""
		self.current_question_index = max(0, self.current_question_index - 1)
		question = self.questions[self.current_question_index]
		self.set_question(question)	

	def on_click_next(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Zmienia pytanie na następne.
		"""
		self.current_question_index = max(0, min(len(self.questions) - 1, self.current_question_index + 1))
		question = self.questions[self.current_question_index]
		self.set_question(question)	

	def on_click_first(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Zmienia pytanie na pierwsze.
		"""
		self.current_question_index = 0
		question = self.questions[self.current_question_index]
		self.set_question(question)	

	def on_click_last(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Zmienia pytanie na ostatnie.
		"""
		self.current_question_index = len(self.questions) - 1
		question = self.questions[self.current_question_index]
		self.set_question(question)	

	def on_click_answer(self, answer: int):
		"""
		Zdarzenie naciśnięcia przycisku odpowiedzi.
		Ustawia wybraną odpowiedz.

		Parametry:
			answer - numer odpowiedzi
		"""
		if self.is_end:
			return
		self.answers[self.current_question_index] = answer
		self.refresh()

	def on_click_check(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Sprawdza poprawność odpowiedzi na wszystkie zadane pytania.
		"""
		if self.is_end:
			return
		self.is_end = True
		correct = 0

		for index, question in enumerate(self.questions):
			answer = self.answers[index]
			if question.check(answer):
				correct += 1

		score_window = TestScoreWindow(self.main_widget, correct, len(self.questions))
		score_window.show()

		question = self.questions[self.current_question_index]
		self.set_question(question)	

	def refresh(self):
		"""
		Odświerza interfejs
		"""
		answer = self.answers[self.current_question_index]
		self.questions_widget.set_highlight(answer)

	def set_question(self, question):
		"""
		Ustawia dane pytanie.

		Parametry:
			question - obiekt klasy TestQuestion
		"""
		self.questions_widget.show_question(question, self.algorithm.name, self.is_end)
		self.refresh()