from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from TestQuestion import TestQuestion
from Styles import Styles
from Widgets.BaseWidget import BaseWidget


class DescriptionLabel(QLabel):
	"""
	Klasa reprezentująca tekstowy panel opisu.

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
		self.setStyleSheet("""
			padding: 10px;
			%s
		""" % Styles.description_background)
		self.setAlignment(Qt.AlignCenter)
		self.setWordWrap(True)
		self.setTextFormat(Qt.RichText)
		self.setMaximumHeight(200)
		self.setMinimumHeight(150)

	def set_text(self, content: str):
		"""
		Ustawia daną treść. 

		Parametry:
		content - Tekst do ustawienia
		"""
		self.setText(content)

	def show_question(self, question: TestQuestion, show_answer=False):
		"""
		Wyświetla pytanie. 

		Parametry:
		question - pytanie, obiekt klasy TestQuestion
		show_answer - określa czy wyświetlić odpowiedz.
		"""

		final_text = "" + question.question + "</br>"
		final_text += "<table>"
		for index, answer in enumerate(question.answers):
			final_text += "<tr>"
			final_text += "<td>" + chr(0x41 + index) + "</td>"
			final_text += "<td>" + answer + "</td>"
			final_text += "</tr>"
			
		if show_answer: 
			final_text += "<tr>"
			final_text += "<td></td>"
			final_text += "<td>" + question.reason + "</td>"
			final_text += "</tr>"
		final_text += "</table>"

		self.set_text(final_text)
