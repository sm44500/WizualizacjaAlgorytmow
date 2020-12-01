from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Styles import Styles


class ControlPanelLabel(QLabel):
	"""
	Klasa reprezentująca pole tekstowe w panelu kontrolnym.

	Parametry:
	parent - rodzic, do którego zostanie podłączony ten widget.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.init_ui()

	def init_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		font = QFont()
		font.setPointSize(14)
		font.setBold(True)
		self.setFont(font)
		self.setMinimumHeight(20)
		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet(Styles.label_background)
