from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

from Visualisation.Visualisation import Visualisation


class BasicAlgorithmVisualisation(Visualisation):
	"""
	Klasa wizualizująca algorytmy proste.

	Parametry:
	snapshots - referencja do wszystkich kroków.
	description_widget - widget w którym wyświetlane są opisy poszczególnych kroków.
	"""

	def __init__(self, snapshots, description_widget):
		super().__init__(snapshots, description_widget)
		self.figure = None
		self.canvas = None
		self.init_ui()

	def init_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		grid = QGridLayout()
		self.setLayout(grid)
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		grid.addWidget(self.canvas)

	def render_snapshot(self):
		"""
		Wyrysowanie aktualnego kroku, jeżeli istnieje.
		"""
		if len(self.snapshots) == 0:
			return

		current_snapshot = self.snapshots[self.current_snapshot_index]
		data_range = range(len(current_snapshot.data))
		data_ids = ["__empty_left", *[data_id for data_id in data_range], "__empty_right"]
		self.figure.clf()
		self.description_widget.set_text(current_snapshot.description)

		nodes = nx.Graph()
		nodes.add_nodes_from(data_ids)

		position = dict()
		position.update((element, (i, 1)) for i, element in enumerate(data_ids))

		axes = plt.axes([0.0, 0.0, 1.0, 1.0])

		node_size = [0.0, *[500.0+60.0*(len(current_snapshot.data[i])+1)**2 for i in data_range], 0.0]

		colors = list()
		colors.append('b')
		for i in data_range:
			colors.append(current_snapshot.highlights[i])
		colors.append('b')

		labels = dict()
		labels["__empty_left"] = " "
		for i in data_range:
			labels[i] = current_snapshot.data[i]
		labels["__empty_right"] = " "

		nx.draw(nodes, labels=labels, pos=position, with_labels=True, node_size=node_size, ax=axes, node_color=colors)
		self.canvas.draw_idle()
