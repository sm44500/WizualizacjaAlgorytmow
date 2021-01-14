from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor, QIcon
from Styles import Styles


class AnswerButton(QPushButton):
	"""
	Kontrolka, przycisk odpowiedzi.

	Parametry:
		parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.label = None
		self.raw_text = ""
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""

		self.setStyleSheet(Styles.button_background)
		self.setMinimumHeight(48)
		self.setContentsMargins(5, 0, 5, 0)
		self.setIconSize(QSize(48, 48))

		shadow = QGraphicsDropShadowEffect()
		shadow.setOffset(1.0, 1.0)
		shadow.setColor(QColor(127, 127, 127, 255))

		self.label = QLabel()
		self.label.setStyleSheet(Styles.button_label)
		self.label.setGraphicsEffect(shadow)
		self.label.setAlignment(Qt.AlignVCenter)
		self.label.setMinimumHeight(self.minimumHeight())

		layout = QVBoxLayout(self)
		layout.addWidget(self.label)
		layout.setContentsMargins(48 + 5, 0, 0, 0)

	def set_icon(self, icon_path):
		"""
		Ustawia ikonę.

		Parametry:
			icon_path - ścieżka do ikony.
		"""
		icon = QIcon(icon_path)
		self.setIcon(icon)

	def set_hint(self, hint):
		"""
		Ustawia podpis.

		Parametry:
			hint - tekst, podpis.
		"""
		self.setToolTip(hint)

	def set_highlight(self, enabled, color=""):
		"""
		Wyróżnia przycisk.

		Parametry:
			enabled - bool, wartość True jeśli wyróżnić, False jeśli nie.
		"""
		text = self.raw_text
		if enabled:
			text = "<b><u>" + self.raw_text + "</u></b>"
		
		if color != "":
			text = "<font color=\"" + color + "\">" + text + "</font>"

		self.label.setText(text)

	def set_text(self, text: str):
		"""
		Ustawia tekst na przycisku.

		Parametry:
			text - tekst do wyświetlenia.
		"""
		self.raw_text = text
		self.label.setText(text)
