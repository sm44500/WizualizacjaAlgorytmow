from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor, QIcon

class ClickableLabel(QLabel):
	"""
	Etykieta z reakcją na kliknięcie
	"""
	clicked = pyqtSignal()
	def __init__(self, parent=None):
		super().__init__(parent)

	def mouseReleaseEvent(self, event):
		"""
		Zdarzenie przyciśnięcia klawisza
		"""
		self.clicked.emit()