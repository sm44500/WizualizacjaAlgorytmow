from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Algorithms.Algorithm import Algorithm
from Paths import Paths

from AlgorithmLoader import *


class AlgorithmsManager:
	def __init__(self, main_widget: QWidget):
		self.algorithms = get_algorithm_list()
		self.main_widget = main_widget
		self.combobox = self.main_widget.top_widget
		self.control_panel = self.main_widget.middle_widget.right_widget
		self.center = self.main_widget.middle_widget.left_widget
		self.bottom = self.main_widget.bottom_widget
		self.current_index = 0
		self.current_algorithm = None
		self.special_widgets = None
		self.setup_algorithms()

	def setup_algorithms(self):
		# Ui
		self.combobox.clear()
		for algorithm in self.algorithms:
			self.combobox.add_algorithms(algorithm.title)

		# Events
		self.main_widget.top_widget.currentIndexChanged.connect(self.on_change_algorithm)

		# Setup
		self.set_algorithm(0)

	def setup_control_panel(self):
		self.control_panel.clear()
		self.description_button = self.control_panel.add_button("Opis", Paths.icon("bookmark.png"))
		self.description_button.clicked.connect(self.show_description)
		self.visualisation_button = self.control_panel.add_button("Wizualizacja", Paths.icon("eye.png"))
		self.visualisation_button.clicked.connect(self.show_visualisation)
		self.questions_button = self.control_panel.add_button("Pytania", Paths.icon("question_mark.png"))

		self.codes_buttons = []
		for index, code in enumerate(self.current_algorithm.codes):
			code_button = self.control_panel.add_button("Kod " + code.language, code.icon)
			code_button.clicked.connect(lambda: self.on_click_code(index))
			self.codes_buttons.append(code_button)

	def on_click_algorithm(self):
		self.current_algorithm.last_value = self.text_box.text()
		self.text_box.clear()

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
		self.bottom.set_text(self.current_algorithm.description)

	def show_visualisation(self):
		self.center.clear_widget()
		self.setup_control_panel()
		self.center.set_visualisation_widget(self.current_algorithm.visualization_widget, self.current_algorithm.snapshots, self.bottom)

		self.special_widgets = list()
		label, self.text_box = self.control_panel.add_text_box()
		self.special_widgets.append(label)
		self.special_widgets.append(self.text_box)

		for name, on_clicked, icon, should_update_current_snapshot in self.current_algorithm.buttons:
			algorithm_button = self.control_panel.add_button(name, icon)
			algorithm_button.clicked.connect(self.on_click_algorithm)
			algorithm_button.clicked.connect(on_clicked)
			if should_update_current_snapshot:
				algorithm_button.clicked.connect(self.center.widget.last_snapshot)
			self.special_widgets.append(algorithm_button)

		left_snapshot_button = self.control_panel.add_button("Poprzedni krok (tymczasowo tutaj)", "")
		left_snapshot_button.clicked.connect(self.center.widget.previous_snapshot)
		self.special_widgets.append(left_snapshot_button)

		right_snapshot_button = self.control_panel.add_button("Nastepny krok (tymczasowo tutaj)", "")
		right_snapshot_button.clicked.connect(self.center.widget.next_snapshot)
		self.special_widgets.append(right_snapshot_button)

		first_snapshot_button = self.control_panel.add_button("Pierwszy krok (tymczasowo tutaj)", "")
		first_snapshot_button.clicked.connect(self.center.widget.first_snapshot)
		self.special_widgets.append(first_snapshot_button)

		last_snapshot_button = self.control_panel.add_button("Ostatni krok (tymczasowo tutaj)", "")
		last_snapshot_button.clicked.connect(self.center.widget.last_snapshot)
		self.special_widgets.append(last_snapshot_button)

	def reset(self):
		self.setup_control_panel()
		self.show_description()

		pass