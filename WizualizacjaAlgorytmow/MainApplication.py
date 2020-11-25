from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Widgets.MainWidget import MainWidget

from Algorithm import Algorithm

WINDOW_TITLE = "Wizualizacja Algorytmów"

class MainApplication(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_algorithms()
        self.setup_events()

    def setup_ui(self):
        #
        # Main window
        #

        # Window config
        self.setObjectName("MainWindow")
        self.resize(800, 620)
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle(WINDOW_TITLE)

        # Main widget
        self.main_widget = MainWidget(self)
        self.main_widget.setObjectName("main_widget")
        self.setCentralWidget(self.main_widget)

    def setup_algorithms(self):
        self.algorithms = [
            Algorithm("example"),
            Algorithm("example_2"),
        ]

        algorithm_combobox = self.main_widget.top_widget
        algorithm_combobox.clear()
        for algorithm in self.algorithms:
            algorithm_combobox.add_algorithms(algorithm.name)

    def setup_events(self):
        self.main_widget.top_widget.currentIndexChanged.connect(self.on_change_algorithm)

    def on_change_algorithm(self):
        print("change!")
        pass

    def set_algorithm(self, index: int):
        pass