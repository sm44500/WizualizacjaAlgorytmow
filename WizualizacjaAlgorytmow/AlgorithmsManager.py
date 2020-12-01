import os
import importlib.util
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Algorithms.Algorithm import Algorithm
from Paths import Paths
from AlgorithmLoader import *
from VisualisationManager import VisualisationManager


class AlgorithmsManager:
	def __init__(self, main_widget: QWidget):
		self.algorithms = get_algorithm_list()
		self.main_widget = main_widget
		self.combobox = self.main_widget.top_widget
		self.control_panel_top = self.main_widget.middle_widget.right_widget.top_control_panel
		self.control_panel_bottom = self.main_widget.middle_widget.right_widget.bottom_control_panel
		self.center = self.main_widget.middle_widget.left_widget
		self.bottom = self.main_widget.bottom_widget
		self.visualisation_manager = None
		self.current_index = 0
		self.current_algorithm = None
		self.setup_algorithms()

	def setup_algorithms(self):
		# Ui
		self.combobox.clear()
		for algorithm in self.algorithms:
			self.combobox.add_algorithms(algorithm.title, algorithm.difficulty)

		# Events
		self.main_widget.top_widget.currentIndexChanged.connect(self.on_change_algorithm)

		# Setup
		self.set_algorithm(0)

	def setup_control_panel(self):
		self.control_panel_top.clear()
		self.control_panel_bottom.clear()

		self.description_button = self.control_panel_top.add_button("Opis", Paths.icon("bookmark.png"))
		self.description_button.clicked.connect(self.show_description)
		self.visualisation_button = self.control_panel_top.add_button("Wizualizacja", Paths.icon("eye.png"))
		self.visualisation_button.clicked.connect(self.show_visualisation)
		self.questions_button = self.control_panel_top.add_button("Pytania", Paths.icon("question_mark.png"))

		self.codes_buttons = []
		for index, code in enumerate(self.current_algorithm.codes):
			code_button = self.control_panel_top.add_button("Kod " + code.language, code.icon)
			code_button.clicked.connect(self.on_click_code)
			self.codes_buttons.append(code_button)

	def on_click_code(self, index):
		QDesktopServices.openUrl(self.current_algorithm.codes[index].url)

	def on_change_algorithm(self, index):
		self.set_algorithm(index)
		pass

	def set_algorithm(self, index):
		self.current_index = index
		self.current_algorithm = self.algorithms[index]
		self.reset()

	def show_description(self):
		self.center.clear_widget()
		self.setup_control_panel()
		self.visualisation_manager = None
		self.bottom.set_text(self.current_algorithm.description)

	def show_visualisation(self):
		self.center.clear_widget()
		self.setup_control_panel()
		self.visualisation_manager = VisualisationManager(self.main_widget, self.current_algorithm)
		
	def reset(self):
		self.setup_control_panel()
		self.visualisation_manager = None
		self.show_description()
		pass