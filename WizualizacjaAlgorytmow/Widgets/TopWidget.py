from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont, QIcon

from Paths import Paths
from Styles import Styles
from Widgets.BaseWidget import BaseWidget


class TopWidget(QComboBox):
	"""
	Klasa reprezentująca górny panel.
	Lista rozwijana.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.difficulty_icons = list()
		self.load_difficulty_icons()
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setStyleSheet(Styles.top_panel_background)
		self.setMinimumHeight(40)
		self.setMaxVisibleItems(5)

		self.setFont(BaseWidget.generate_font())

	def load_difficulty_icons(self):
		for filename in ["easy", "moderate", "difficult"]:
			self.difficulty_icons.append(QIcon(Paths.icon("%s.png" % filename)))

	def add_algorithms(self, algorithm_name: str, algorithm_difficulty: int = 1):
		"""
		Dodaje algorytm do listy rozwijanej.

		Parametry:
			algorithm_name - tytuł algorytmu do dodania.
		"""
		icon_index = max(min(algorithm_difficulty-1, 2), 0)
		self.addItem(self.difficulty_icons[icon_index], algorithm_name)
