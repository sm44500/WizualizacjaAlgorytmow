from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout
from Styles import Styles
from Paths import Paths


class WelcomeWindow(QMainWindow):
	"""
	Okno powitalne programu.

	Parametry:
	parent - widget rodzic.
	"""

	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.setObjectName("WelcomeWindow")
		self.resize(400, 250)
		self.setMinimumSize(QSize(400, 250))
		self.setMaximumSize(QSize(400, 250))
		self.setWindowTitle("WAWI ZUT")

		self.setStyleSheet(Styles.welcome_background)
		self.setWindowIcon(QIcon(Paths.icon("window_icon.png")))

		self.central_widget = QWidget()
		self.grid = QGridLayout()

		self.grid.setRowStretch(0, 5)

		self.setCentralWidget(self.central_widget)
		self.centralWidget().setLayout(self.grid)

		self.grid.addWidget(add_label("WAWI ZUT", 14, True, Qt.AlignCenter), 0, 0)
		self.grid.addWidget(add_label("Wizualizacja Algorytmów", 12, False, Qt.AlignCenter), 1, 0)
		self.grid.addWidget(add_label("Wydział Informatyki", 10, False, Qt.AlignCenter), 2, 0)
		self.grid.addWidget(add_label("Zachodniopomorski Uniwersytet Technologiczny w Szczecinie", 10, False, Qt.AlignCenter), 3, 0)
		self.grid.addWidget(add_label("2021", 10, False, Qt.AlignCenter), 4, 0)


def add_label(text, size, bold, align):
	font = QFont()
	font.setPointSize(size)
	font.setBold(bold)
	label = QLabel()
	label.setFont(font)
	label.setMinimumHeight(20)
	label.setAlignment(align)
	label.setText(text)
	return label
