from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from Styles import Styles
from Widgets.MainWidget import MainWidget
from AlgorithmsManager import AlgorithmsManager

WINDOW_TITLE = "Wizualizacja Algorytmów"

class MainApplication(QMainWindow):
	"""
	Główna klasa aplikacji.
	
	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setup_ui()
		self.algorithms_manager = AlgorithmsManager(self.main_widget)

	def setup_ui(self):
		"""
		Inicjalizacja UI
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
		self.setWindowTitle(WINDOW_TITLE)

		# Main widget
		self.main_widget = MainWidget(self)
		self.main_widget.setObjectName("main_widget")
		self.setStyleSheet(Styles.main_background)
		self.setCentralWidget(self.main_widget)

	