from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel

from Styles import Styles
from Widgets.ControlPanel import ControlPanel
from Widgets.BaseWidget import BaseWidget


class RightPanel(BaseWidget):
	"""
	Klasa reprezentująca prawy panel.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QVBoxLayout)
		self.top_control_panel = None
		self.bottom_control_panel = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setMaximumWidth(250)
		self.setMinimumWidth(220)

		self.top_control_panel = ControlPanel(self, Qt.AlignTop)
		self.__generate_label_background(Styles.right_panel_background).setParent(self.top_control_panel)

		self.bottom_control_panel = ControlPanel(self, Qt.AlignBottom)
		self.__generate_label_background(Styles.right_panel_background).setParent(self.bottom_control_panel)

		self.widget_layout.addWidget(self.top_control_panel)
		self.widget_layout.addWidget(self.bottom_control_panel)

	@staticmethod
	def __generate_label_background(style: str) -> QLabel:
		"""
		Wygenerowanie pustego pola, które posłuży za tło

		Parametry:
		style - style w jakim zostanie wygenerowane tło.

		Zwracany typ:
		QLabel
		"""
		label = QLabel()
		label.setStyleSheet(style)
		label.setAlignment(Qt.AlignCenter)
		label.setText(" ")

		return label
