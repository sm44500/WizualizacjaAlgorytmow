from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QIcon
from Paths import Paths
from AlgorithmsLogic import Algorithm
from Settings import Settings
from Styles import Styles


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
		self.play_icon = Paths.icon("play.png")
		self.pause_icon = Paths.icon("pause.png")
		self.text_box_label = None
		self.text_box = None
		self.icon_panel = None
		self.first_step_button = None
		self.previous_step_button = None
		self.next_step_button = None
		self.last_snapshot_button = None
		self.play_button = None
		self.slider = None
		self.is_playing = False
		self.setup_control_panel()
		self.current_snapshot_index = 0
		self.update_playing_button()

	def setup_control_panel(self):
		"""
		Inicjalizuje panel kontrolny.
		"""
		self.center.set_widget(self.algorithm.visualization_widget)

		for control in self.algorithm.controls:
			control_type = control[0]
			if control_type == "BUTTON":
				title, callback, icon, hint, update = control[1:]
				button = self.control_panel_bottom.add_button(title, icon)
				button.clicked.connect(callback)
				if update:
					button.clicked.connect(self.on_click_last_snapshot)
				button.set_hint(hint)
				self.internal_widgets.append(button)
			elif control_type == "TEXTBOX":
				label_text, callback, hint, update = control[1:]
				label = self.control_panel_bottom.add_label(label_text)
				textbox = self.control_panel_bottom.add_text_box(hint)
				textbox.textChanged.connect(callback)
				if update:
					textbox.textChanged.connect(self.on_click_last_snapshot)
				self.internal_widgets.append(label)
				self.internal_widgets.append(textbox)
			else:
			 	print("Unknown control type")

		self.icon_panel = self.control_panel_bottom.add_icon_panel()

		self.first_step_button = self.icon_panel.add_button(Paths.icon("first.png"), "Uruchomienie pierwszego kroku.")
		self.first_step_button.clicked.connect(self.on_click_first_step)

		self.previous_step_button = self.icon_panel.add_button(Paths.icon("backward.png"), "Uruchomienie poprzedniego kroku.")
		self.previous_step_button.clicked.connect(self.on_click_previous_step)

		self.play_button = self.icon_panel.add_button(Paths.icon("play.png"))
		self.play_button.clicked.connect(self.on_click_play)

		self.next_step_button = self.icon_panel.add_button(Paths.icon("forward.png"), "Uruchomienie następnego kroku.")
		self.next_step_button.clicked.connect(self.on_click_next_step)

		self.last_snapshot_button = self.icon_panel.add_button(Paths.icon("last.png"), "Uruchomienie ostatniego kroku.")
		self.last_snapshot_button.clicked.connect(self.on_click_last_snapshot)


	def on_click_first_step(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Uruchomienie pierwszego kroku, jeżeli istnieje.
		"""
		self.stop_changing_snapshots()
		self.current_snapshot_index = 0
		snapshot = self.algorithm.snapshots[self.current_snapshot_index]
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_previous_step(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Uruchomienie poprzedniego kroku, jeżeli istnieje.
		"""
		self.stop_changing_snapshots()
		self.current_snapshot_index = max(0, min(self.current_snapshot_index-1, len(self.algorithm.snapshots)-1))
		snapshot = self.algorithm.snapshots[self.current_snapshot_index]
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_next_step(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Uruchomienie następnego kroku, jeżeli istnieje.
		"""
		self.stop_changing_snapshots()
		self.current_snapshot_index = max(0, min(self.current_snapshot_index+1, len(self.algorithm.snapshots)-1))
		snapshot = self.algorithm.snapshots[self.current_snapshot_index]
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_last_snapshot(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Uruchomienie ostatniego kroku, jeżeli istnieje.
		"""
		self.stop_changing_snapshots()
		self.current_snapshot_index = max(0, min(len(self.algorithm.snapshots) - 1, len(self.algorithm.snapshots)))
		snapshot = self.algorithm.snapshots[self.current_snapshot_index]
		self.description_widget.set_text(snapshot.description)
		self.center.widget.render_snapshot(snapshot)

	def on_click_play(self):
		"""
		Zdarzenie naciśnięcia przycisku.
		Automatycznie odtwarza algorytm krok po kroku.
		Prędkość odtwarzania zależy od pozycji suwaka (1-100) ms na każdy znak w opisie.
		"""
		self.is_playing = not self.is_playing
		self.update_playing_button()
		for i in range(len(self.algorithm.snapshots) - self.current_snapshot_index - 1):
			if self.is_playing:
				self.current_snapshot_index = max(0, min(self.current_snapshot_index+1, len(self.algorithm.snapshots)-1))
				snapshot = self.algorithm.snapshots[self.current_snapshot_index]
				self.description_widget.set_text(snapshot.description)
				self.center.widget.render_snapshot(snapshot)
				QTest.qWait((100 - Settings.visualisation_speed[0]) * len(snapshot.description))
		self.stop_changing_snapshots()

	def stop_changing_snapshots(self):
		"""
		Wyłączenie przełączania pomiędzy krokami automatycznie.
		"""
		self.is_playing = False
		self.update_playing_button()

	def update_playing_button(self):
		"""
		Zaktualizowanie ikony klawiszu odpowiedzialnego za automatyczne wyświetlanie kroków.
		"""
		if not self.is_playing:
			self.play_button.set_icon(self.play_icon)
			self.play_button.set_hint("Rozpoczęcie automatycznego odtwarzania kroków.")
			self.play_button.setStyleSheet(Styles.snapshot_button_background)
		else:
			self.play_button.set_icon(self.pause_icon)
			self.play_button.set_hint("Zatrzymanie automatycznego odtwarzania kroków.")
			self.play_button.setStyleSheet(Styles.snapshot_button_background_clicked)

	def on_update_slider(self):
		self.stop_changing_snapshots()
		self.on_click_play()
