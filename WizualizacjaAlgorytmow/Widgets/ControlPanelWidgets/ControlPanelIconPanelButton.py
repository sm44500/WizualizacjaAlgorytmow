from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class ControlPanelIconPanelButton(QPushButton):
	"""
	Kontrolka panelu z ikonami. Przycisk z ikoną.

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
		font = QFont()
		font.setFixedPitch(True)
		self.setStyleSheet("""
			padding-left: 5px;
			padding-right: 5px;
			text-align: left;
			background-color: #dcdcdc;
		""")
		font.setPointSize(16)
		font.setBold(False)
		font.setFixedPitch(True)
		self.setFont(font)
		self.setFixedHeight(32)
		self.setFixedWidth(32)

	def set_icon(self, icon_path):
		icon = QIcon(icon_path)
		self.setIcon(icon)
		self.setIconSize(QSize(24, 24))