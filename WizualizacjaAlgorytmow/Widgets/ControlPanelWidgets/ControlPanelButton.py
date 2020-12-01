from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Styles import Styles


class ControlPanelButton(QPushButton):
	"""
	Kontrolka panelu kontrolnego. Przycisk.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.label = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""

		self.setStyleSheet(Styles.button_background)
		self.setMinimumHeight(32)
		self.setContentsMargins(5, 0, 5, 0)

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
		layout.setContentsMargins(24 + 5, 0, 0, 0)

	def set_icon(self, icon_path):
		icon = QIcon(icon_path)
		self.setIcon(icon)
		self.setIconSize(QSize(24, 24))

	def set_text(self, text: str):
		# self.setText(text)
		self.label.setText(text)
