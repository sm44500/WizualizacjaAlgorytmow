from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSizePolicy, QGraphicsDropShadowEffect

from Paths import Paths
from Styles import Styles
from Widgets.ControlPanel import ControlPanel


class TestScoreWindow(QMainWindow):
	"""
	Okno odpowiedzialne za wyświetlanie wyniku uzyskanego przez użytkownika.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None, correct_answers: int = 0, total_answers: int = 1):
		super().__init__(parent)
		self.score_label = None
		self.hint_label = None
		self.window_title = "Wynik testu"
		self.score = "%.0f%%" % (100.0 * correct_answers / total_answers)
		self.hint = "Uzyskałeś %s poprawnych odpowiedzi na %s możliwych." % (correct_answers, total_answers)
		self.score_color_style = """QLabel { color: %s }""" % ("#ee3333" if total_answers*0.5 >= correct_answers else "#33ee33")
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setObjectName("TestScoreWindow")

		self.setSizePolicy(self.get_size_policy())
		self.setMinimumSize(QSize(500, 110))
		self.setWindowTitle(self.window_title)
		self.setWindowIcon(QIcon(Paths.icon("window_icon.png")))
		self.setStyleSheet(Styles.test_score_window_style)

		shadow = QGraphicsDropShadowEffect()
		shadow.setXOffset(0)
		shadow.setYOffset(5)
		shadow.setBlurRadius(10)

		self.control_panel = ControlPanel(self, Qt.AlignTop)

		self.score_label = self.control_panel.add_label(self.score)
		self.score_label.setStyleSheet(Styles.test_score_window_label_score_style + self.score_color_style)
		self.score_label.setGraphicsEffect(shadow)

		self.hint_label = self.control_panel.add_label(self.hint)
		self.hint_label.setStyleSheet(Styles.test_score_window_label_hint_style)

		self.setCentralWidget(self.control_panel)

	def get_size_policy(self):
		size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		size_policy.setHorizontalStretch(1)
		size_policy.setVerticalStretch(1)
		size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

		return size_policy
