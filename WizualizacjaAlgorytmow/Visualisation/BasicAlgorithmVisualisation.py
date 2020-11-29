import math

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

		self.figure.clf()
		self.description_widget.set_text(current_snapshot.description)

		nodes = nx.Graph()
		nodes.add_nodes_from(current_snapshot.data)

		position = dict()
		position.update((element, (i, 1)) for i, element in enumerate(current_snapshot.data))

		axes = plt.axes([0.0, 0.0, 1.0, 1.0])

		node_size = [500.0+60.0*(math.log10(abs(i)+1)+1)**2 for i in current_snapshot.data]

		colors = list()
		for i in range(len(current_snapshot.data)):
			colors.append(current_snapshot.highlights[i])

		nx.draw(nodes, pos=position, with_labels=True, node_size=node_size, ax=axes, node_color=colors)
		self.canvas.draw_idle()
