from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Paths import Paths
from Algorithms.Algorithm import Algorithm

class VisualisationManager:
	"""
	Kontroler odpowiadający za wizualizację algorytmów.

	Parametry:
	main_widget - referencja do głównego widget'u.
	algorithm - obiekt algorytmu.
	"""
	def __init__(self, main_widget: QWidget, algorithm: Algorithm):
		self.algorithm = algorithm
		self.main_widget = main_widget
		self.control_panel_bottom = self.main_widget.middle_widget.right_widget.bottom_control_panel
		self.center = self.main_widget.middle_widget.left_widget
		self.description_widget = self.main_widget.bottom_widget
		self.internal_widgets = []
		self.setup_control_panel()

	def setup_control_panel(self):
		self.center.set_widget(self.algorithm.visualization_widget)

		self.text_box_label = self.control_panel_bottom.add_label("Wartość elementu:")
		self.text_box = self.control_panel_bottom.add_text_box()

		for name, on_clicked, icon, should_update_current_snapshot in self.algorithm.buttons:
			algorithm_button = self.control_panel_bottom.add_button(name, icon)
			algorithm_button.clicked.connect(self.on_click_algorithm)
			algorithm_button.clicked.connect(on_clicked)
			if should_update_current_snapshot:
				algorithm_button.clicked.connect(self.on_click_last_snapshot)
			self.internal_widgets.append(algorithm_button)

		self.icon_panel = self.control_panel_bottom.add_icon_panel()

		self.first_step_button = self.icon_panel.add_button(Paths.icon("first.png"))
		self.first_step_button.clicked.connect(self.on_click_first_step)

		self.previous_step_button = self.icon_panel.add_button(Paths.icon("backward.png"))
		self.previous_step_button.clicked.connect(self.on_click_previous_step)

		self.execute_button = self.icon_panel.add_button(Paths.icon("play.png"))
		self.execute_button.clicked.connect(self.on_click_play)

		self.next_step_button = self.icon_panel.add_button(Paths.icon("forward.png"))
		self.next_step_button.clicked.connect(self.on_click_next_step)

		self.last_snapshot_button = self.icon_panel.add_button(Paths.icon("last.png"))
		self.last_snapshot_button.clicked.connect(self.on_click_last_snapshot)

	def on_click_first_step(self):
		"""
		Uruchomienie pierwszego kroku, jeżeli istnieje.
		"""
		snapshot = self.algorithm.first_snapshot()
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_previous_step(self):
		"""
		Uruchomienie poprzedniego kroku, jeżeli istnieje.
		"""
		snapshot = self.algorithm.previous_snapshot()
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_next_step(self):
		"""
		Uruchomienie następnego kroku, jeżeli istnieje.
		"""
		snapshot = self.algorithm.next_snapshot()
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_last_snapshot(self):
		"""
		Uruchomienie ostatniego kroku, jeżeli istnieje.
		"""
		snapshot = self.algorithm.last_snapshot()
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_algorithm(self):
		self.algorithm.last_value = self.text_box.text()
		self.description_widget.set_text(snapshot.description)
		self.text_box.clear()

	def on_click_play(self):
		pass