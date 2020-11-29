from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Widgets.TopWidget import TopWidget
from Widgets.MiddleWidget import MiddleWidget
from Widgets.BottomWidget import BottomWidget

class MainWidget(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setup_ui()

	def setup_ui(self):
		self.widget_layout = QVBoxLayout(self)
		self.widget_layout.setContentsMargins(5, 5, 5, 5)
		self.widget_layout.setSpacing(0)
		
		self.top_widget = TopWidget(self)
		self.middle_widget = MiddleWidget(self)
		self.bottom_widget = BottomWidget(self)

		self.widget_layout.addWidget(self.top_widget, 1)
		self.widget_layout.addWidget(self.middle_widget, 60)
		self.widget_layout.addWidget(self.bottom_widget, 30)
		self.setLayout(self.widget_layout)