from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Styles import Styles
from Widgets.ControlPanel import ControlPanel


class RightPanel(QWidget):
	"""
	Klasa reprezentująca prawy panel.

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
		self.setMaximumWidth(250)
		self.setMinimumWidth(220)
		self.widget_layout = QVBoxLayout(self)
		self.widget_layout.setContentsMargins(0, 0, 0, 0)
		self.widget_layout.setSpacing(0)

		self.top_control_panel = ControlPanel(self, Qt.AlignTop)
		self.__generate_label_background(Styles.right_panel_background).setParent(self.top_control_panel)

		self.bottom_control_panel = ControlPanel(self, Qt.AlignBottom)
		self.__generate_label_background(Styles.right_panel_background).setParent(self.bottom_control_panel)

		self.widget_layout.addWidget(self.top_control_panel)
		self.widget_layout.addWidget(self.bottom_control_panel)
		self.setLayout(self.widget_layout)

	def __generate_label_background(self, style: str):
		label = QLabel()
		label.setStyleSheet(style)
		label.setAlignment(Qt.AlignCenter)
		label.setText(" ")

		return label
