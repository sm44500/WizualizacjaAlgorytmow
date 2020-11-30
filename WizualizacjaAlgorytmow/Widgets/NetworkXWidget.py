import matplotlib.pyplot as plt
import networkx as nx

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Snapshot import Snapshot

class NetworkXWidget(QWidget):
	"""
	Widget wizualuzacji opertej na bibliotece NetworkX.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.widget_layout = QGridLayout(self)
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.widget_layout.addWidget(self.canvas)
		pass

	def render_snapshot(self, snapshot: Snapshot):
		"""
		Wyświetla aktualnegy stan algorytmu.

		Parametry:
		snapshot - aktualny stan algorytmu. Obiekt typu Snapshot.
		"""
		data_range = range(len(snapshot.data))
		data_ids = ["__empty_left", *[data_id for data_id in data_range], "__empty_right"]
		self.figure.clf()

		nodes = nx.Graph()
		nodes.add_nodes_from(data_ids)

		position = dict()
		position.update((element, (i, 1)) for i, element in enumerate(data_ids))

		axes = plt.axes([0.0, 0.0, 1.0, 1.0])

		node_size = [0.0, *[500.0+60.0*(len(snapshot.data[i])+1)**2 for i in data_range], 0.0]

		colors = list()
		colors.append('b')
		for i in data_range:
			colors.append(snapshot.highlights[i])
		colors.append('b')

		labels = dict()
		labels["__empty_left"] = " "
		for i in data_range:
			labels[i] = snapshot.data[i]
		labels["__empty_right"] = " "

		nx.draw(nodes, labels=labels, pos=position, with_labels=True, node_size=node_size, ax=axes, node_color=colors)
		self.canvas.draw_idle()
