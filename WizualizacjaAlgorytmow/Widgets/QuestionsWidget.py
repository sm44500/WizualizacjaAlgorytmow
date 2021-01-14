import os
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from TestQuestion import TestQuestion
from Styles import Styles
from Widgets.AnswerButton import AnswerButton
from Widgets.BaseWidget import BaseWidget
from Paths import Paths


class QuestionsWidget(BaseWidget):
	"""
	Klasa reprezentująca centralny panel aplikacji.

	Parametry:
		parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QVBoxLayout)
		self.image = None
		self.question = None
		self.explanation = None
		self.answers = []
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.image = QLabel(self)
		self.image.setAlignment(Qt.AlignCenter)
		self.widget_layout.addWidget(self.image)
		

		self.question = QLabel(self)
		self.question.setWordWrap(True)
		self.question.setAlignment(Qt.AlignCenter)
		self.widget_layout.addWidget(self.question)

		self.explanation = QLabel(self)
		self.explanation.setWordWrap(True)
		self.explanation.setAlignment(Qt.AlignCenter)
		self.widget_layout.addWidget(self.explanation)

		for l in ["A", "B", "C", "D"]:
			answer = AnswerButton(self)
			answer.set_icon(Paths.icon("letter_%s.png" % l.lower()))
			answer.set_hint("Odpowiedź %s" % l)
			self.answers.append(answer)
			self.widget_layout.addWidget(answer)

		self.setStyleSheet(Styles.description_background)

	def show_question(self, question: TestQuestion, algorithm, show_explanation=False):
		"""
		Wyświetla pytanie.

		Parametry:
			parent - widget rodzic.

			question - pytanie, obiekt klasy TestQuestion.

			algorithm - nazwa algorytmu

			show_explanation - określa czy wyświetlić uzasadnienie.
		"""

		self.question.setText(question.question)

		image_path = Paths.test_question_image(algorithm, question.image)
		if not os.path.isfile(image_path):
			image_path = Paths.icon("question_mark.png")

		pixels = QPixmap(image_path)
		self.image.setPixmap(pixels)
		self.image.resize(pixels.width(), pixels.height())

		if show_explanation:
			self.explanation.setText(question.explanation)

		for index, answer in enumerate(question.answers):
			button = self.answers[index]
			button.set_text(answer)
			

	def set_highlight(self, answer_index=-1, show_answer=-1):
		"""
		Wyróżnia odpowiedź.

		Parametry:
			answer_index - numer odpowiedzi.
		"""
		for index, answer_button in enumerate(self.answers):
			color = ""
			if show_answer != -1:
				color = "#b82c2c"
				if index == show_answer:
					color = "#45de54"

			if index == answer_index:
				answer_button.set_highlight(True, color)
			else:
				answer_button.set_highlight(False, color)