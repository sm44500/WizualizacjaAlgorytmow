from PyQt5.QtWidgets import QLabel

from TestQuestion import TestQuestion
from Styles import Styles
from Widgets.BaseWidget import BaseWidget


class BottomWidget(QLabel):
	"""
	Klasa reprezentująca dolny panel.

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
		font = BaseWidget.generate_font()
		self.setStyleSheet("""
			padding: 10px;
			%s
		""" % Styles.description_background)
		self.setFont(font)
		self.setWordWrap(True)
		self.setMaximumHeight(200)
		self.setMinimumHeight(150)

	def set_text(self, content: str):
		self.setText(content)

	def show_question(self, question: TestQuestion):
		self.set_text(question.question)
