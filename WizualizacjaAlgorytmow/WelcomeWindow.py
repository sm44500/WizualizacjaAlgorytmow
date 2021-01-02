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
		self.resize(400, 350)
		self.setMinimumSize(QSize(400, 350))
		self.setMaximumSize(QSize(400, 350))
		self.setWindowTitle("WAWI ZUT")

		self.setStyleSheet(Styles.welcome_background)
		self.setWindowIcon(QIcon(Paths.icon("window_icon.png")))

		self.central_widget = QWidget()
		self.grid = QGridLayout()

		self.setCentralWidget(self.central_widget)
		self.centralWidget().setLayout(self.grid)

		self.logo = QLabel(self)
		self.logo.setPixmap(QPixmap(Paths.icon("logo.png")))
		self.logo.setAlignment(Qt.AlignCenter)
		self.grid.addWidget(self.logo, 0, 0)

		self.grid.addWidget(add_label("\nWizualizacja Algorytmów", 12, False, Qt.AlignCenter), 1, 0)
		self.grid.addWidget(add_label("Wydział Informatyki \nZachodniopomorski Uniwersytet Technologiczny w Szczecinie\n", 10, False, Qt.AlignCenter), 2, 0)
		self.grid.addWidget(add_label("Oprogramowanie zrealizowane w ramach przedmiotu \nInżynierski Projekt Zespołowy 1", 10, False, Qt.AlignCenter), 3, 0)
		self.grid.addWidget(add_label("Autorzy: Marcin Jakubowski, Aliaksei Kavaliou, Piotr Podleżański, \nMateusz Smolarkiewicz, Łukasz Więckowski, Mykhailo Yelmikheiev", 10, False, Qt.AlignLeft), 4, 0)
		self.grid.addWidget(add_label("Opiekun projektu: dr hab.inż. Imed El Fray", 10, False, Qt.AlignLeft), 5, 0)
		self.grid.addWidget(add_label("Konsultacja merytoryczna: dr hab.inż. Imed El Fray, \nmgr inż. Włodzimierz Chocianowicz, mgr inż. Gerard Wawrzyniak", 10, False, Qt.AlignLeft), 6, 0)


def add_label(text, size, bold, align):
	font = QFont()
	font.setPointSize(size)
	font.setBold(bold)
	label = QLabel()
	label.setFont(font)
	label.setAlignment(align)
	label.setText(text)
	return label
