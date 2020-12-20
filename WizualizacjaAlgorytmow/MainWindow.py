from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from Styles import Styles
from Widgets.MainWidget import MainWidget
from AlgorithmsManager import AlgorithmsManager
from Paths import Paths


class MainWindow(QMainWindow):
	"""
	Główne okno aplikacji.
	
	Parametry:
		parent - widget rodzic.
	"""
	window_title = "Wizualizacja Algorytmów"

	def __init__(self, parent=None):
		super().__init__(parent)
		self.setup_ui()
		self.algorithms_manager = AlgorithmsManager(self.main_widget)
		self.main_widget = None

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		# Window config
		self.setObjectName("MainWindow")
		self.resize(800, 620)
		size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		size_policy.setHorizontalStretch(1)
		size_policy.setVerticalStretch(1)
		size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(size_policy)
		self.setMinimumSize(QSize(1280, 720))
		self.setWindowTitle(MainWindow.window_title)

		# Main widget
		self.main_widget = MainWidget(self)
		self.main_widget.setObjectName("main_widget")
		self.setStyleSheet(Styles.main_background)
		self.setCentralWidget(self.main_widget)
		self.setWindowIcon(QIcon(Paths.icon("window_icon.png")))
