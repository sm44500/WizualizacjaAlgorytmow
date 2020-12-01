from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont, QIcon
from Styles import Styles


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
		self.setStyleSheet(Styles.snapshot_button_background)
		font.setPointSize(16)
		font.setBold(False)
		font.setFixedPitch(True)
		self.setFont(font)
		self.setFixedHeight(32)
		self.setFixedWidth(32)
		self.setIconSize(QSize(24, 24))

	def set_icon(self, icon_path):
		icon = QIcon(icon_path)
		self.setIcon(icon)

	def set_hint(self, hint):
		self.setToolTip(hint)