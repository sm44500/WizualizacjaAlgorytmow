from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class BaseWidget(QWidget):
	"""
	Bazowa klasa reprezentująca widget posiadająca wspólne cechy wszystkich widget'ów.

	Parametry:
		parent - widget rodzic.
		layout_type - typ layout'u jaki ma zostać domyślnie wygenerowany.

	"""
	def __init__(self, parent=None, layout_type=QHBoxLayout):
		super().__init__(parent)
		self.widget_layout = None
		self.setup_widget(layout_type)

	def setup_widget(self, layout_type):
		"""
		Inicjalizacja podstawowych elementów widget'u.
		"""
		self.widget_layout = layout_type(self)
		self.widget_layout.setContentsMargins(0, 0, 0, 0)
		self.widget_layout.setSpacing(0)

		self.setLayout(self.widget_layout)

	@staticmethod
	def generate_font() -> QFont:
		"""
		Wygenerowanie najczęściej używanej czcionki.
		"""
		font = QFont()
		font.setPointSize(20)
		font.setBold(True)

		return font
