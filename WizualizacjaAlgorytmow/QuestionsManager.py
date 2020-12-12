import random
from PyQt5.QtWidgets import QWidget, QMessageBox
from Paths import Paths
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
		self.description_widget = self.main_widget.bottom_widget
		self.answer_buttons = []
		self.answers = [-1] * len(self.questions)
		self.is_end = False
		self.setup_control_panel()
		self.current_question_index = 0
		random.shuffle(self.questions)
		self.set_question(self.questions[self.current_question_index])

	def setup_control_panel(self):
		"""
		Inicjalizuje panel kontrolny.
		"""
		self.check_button = self.control_panel_bottom.add_button("Sprawdź", Paths.icon("eye.png"), "Sprawdza test")
		self.check_button.clicked.connect(self.on_click_check)

		self.answer_icon_panel = self.control_panel_bottom.add_icon_panel()

		answer_button = self.answer_icon_panel.add_button(Paths.icon("letter_a.png"), "Odpowiedź A")
		answer_button.clicked.connect(lambda: self.on_click_answer(0))
		self.answer_buttons.append(answer_button)

		answer_button = self.answer_icon_panel.add_button(Paths.icon("letter_b.png"), "Odpowiedź B")
		answer_button.clicked.connect(lambda: self.on_click_answer(1))
		self.answer_buttons.append(answer_button)

		answer_button = self.answer_icon_panel.add_button(Paths.icon("letter_c.png"), "Odpowiedź C")
		answer_button.clicked.connect(lambda: self.on_click_answer(2))
		self.answer_buttons.append(answer_button)

		answer_button = self.answer_icon_panel.add_button(Paths.icon("letter_d.png"), "Odpowiedź D")
		answer_button.clicked.connect(lambda: self.on_click_answer(3))
		self.answer_buttons.append(answer_button)

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
				correct+=1

		question_count = len(self.questions)
		msg_box = QMessageBox(self.main_widget)
		msg_box.setWindowTitle("Wynik")
		msg_box.setText("Uzyskałeś %s dobrych odpowiedzi na %s możliwych." % (correct, question_count))
		msg_box.setStandardButtons(QMessageBox.Ok)
		msg_box.show()

		question = self.questions[self.current_question_index]
		self.set_question(question)	

	def refresh(self):
		"""
		Odświerza interfejs
		"""
		answer = self.answers[self.current_question_index]
		for index, answer_button in enumerate(self.answer_buttons): 
			if index == answer:
				answer_button.set_highlight(True)
			else:
				answer_button.set_highlight(False)

	def set_question(self, question):
		"""
		Ustawia dane pytanie.

		Parametry:
		question - obiekt klasy TestQuestion
		"""
		self.description_widget.show_question(question, self.is_end)
		self.refresh()