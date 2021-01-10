from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout
from Styles import Styles
from Paths import Paths

WINDOW_SIZE_X = 415
WINDOW_SIZE_Y = 400

class WelcomeWindow(QMainWindow):
	"""
	Okno powitalne programu.
	"""

	def __init__(self):
		QMainWindow.__init__(self)
		self.setObjectName("WelcomeWindow")
		self.resize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
		self.setMinimumSize(QSize(WINDOW_SIZE_X, WINDOW_SIZE_Y))
		self.setMaximumSize(QSize(WINDOW_SIZE_X, WINDOW_SIZE_Y))
		self.setWindowTitle("WAWI ZUT")

		self.setStyleSheet(Styles.welcome_background)
		self.setWindowIcon(QIcon(Paths.icon("window_icon.png")))

		self.central_widget = QWidget()
		self.layout = QVBoxLayout()

		self.setCentralWidget(self.central_widget)
		self.centralWidget().setLayout(self.layout)

		self.logo = QLabel(self)
		self.logo.setPixmap(QPixmap(Paths.icon("logo.png")))
		self.logo.setAlignment(Qt.AlignCenter)
		self.layout.addWidget(self.logo, 10)

		self.layout.addWidget(add_label("\nWizualizacja Algorytmów", 12, False, Qt.AlignCenter), 10)
		self.layout.addWidget(add_label("Wydział Informatyki \nZachodniopomorski Uniwersytet Technologiczny w Szczecinie\n", 10, False, Qt.AlignCenter), 1)
		self.layout.addWidget(add_label("Oprogramowanie zrealizowane w ramach przedmiotu \nInżynierski Projekt Zespołowy 1", 10, False, Qt.AlignCenter), 1)
		self.layout.addWidget(add_label("Autorzy: Marcin Jakubowski, Aliaksei Kavaliou, Piotr Podleżański, \nMateusz Smolarkiewicz, Łukasz Więckowski, Mykhailo Yelmikheiev", 10, False, Qt.AlignLeft), 1)
		self.layout.addWidget(add_label("Opiekun projektu: dr hab.inż. Imed El Fray", 10, False, Qt.AlignLeft), 1)
		self.layout.addWidget(add_label("Konsultacja merytoryczna: dr hab.inż. Imed El Fray, \nmgr inż. Włodzimierz Chocianowicz, mgr inż. Gerard Wawrzyniak", 10, False, Qt.AlignLeft), 1)


def add_label(text, size, bold, align):
	font = QFont("Helvetica")
	font.setPointSize(size)
	font.setBold(bold)
	label = QLabel()
	label.setFont(font)
	label.setAlignment(align)
	label.setText(text)
	return label
