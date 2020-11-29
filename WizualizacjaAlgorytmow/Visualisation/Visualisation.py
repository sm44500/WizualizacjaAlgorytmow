from PyQt5.QtWidgets import *


class Visualisation(QWidget):
	"""
	Klasa abstrakcyjna odpowiadająca za wizualizację algorytmów.

	Parametry:
	snapshots - referencja do wszystkich kroków.
	description_widget - widget w którym wyświetlane są opisy poszczególnych kroków.
	"""
	def __init__(self, snapshots, description_widget):
		super().__init__()
		self.description_widget = description_widget
		self.snapshots = snapshots
		self.current_snapshot_index = 0

	def next_snapshot(self):
		"""
		Uruchomienie następnego kroku, jeżeli istnieje.
		"""
		self.current_snapshot_index = min(self.current_snapshot_index+1, len(self.snapshots)-1)
		self.render_snapshot()

	def previous_snapshot(self):
		"""
		Uruchomienie poprzedniego kroku, jeżeli istnieje.
		"""
		self.current_snapshot_index = max(self.current_snapshot_index-1, 0)
		self.render_snapshot()

	def render_snapshot(self):
		"""
		Wyrysowanie aktualnego kroku, jeżeli istnieje.
		"""
		pass
