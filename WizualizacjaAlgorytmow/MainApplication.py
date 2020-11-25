from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Widgets.MainWidget import MainWidget

WINDOW_TITLE = "Wizualizacja Algorytmów"

algorithms = [

]

class MainApplication(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

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
