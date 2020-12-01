import math

import matplotlib.pyplot as plt
import networkx as nx

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Snapshot import Snapshot
from Styles import Styles


class NetworkXWidget(QWidget):
	"""
	Widget wizualuzacji opartej na bibliotece NetworkX.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.widget_layout = None
		self.figure = None
		self.canvas = None
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.widget_layout = QGridLayout(self)
		self.figure = plt.figure()
		self.figure.set_facecolor("#00000F")
		self.canvas = FigureCanvas(self.figure)
		self.setStyleSheet(Styles.description_background)
		self.widget_layout.setContentsMargins(0, 0, 0, 0)
		self.widget_layout.addWidget(self.canvas)
		pass

	def render_snapshot(self, snapshot: Snapshot):
		"""
		Wyświetla aktualny stan algorytmu.

		Parametry:
		snapshot - aktualny stan algorytmu. Obiekt typu Snapshot.
		"""
		data_range = range(len(snapshot.data))
		data_ids = [data_id for data_id in data_range]
		data_indexes = ["index_%i" % index for index in data_range]

		self.figure.clf()

		nodes = nx.Graph()
		nodes2 = nx.Graph()
		nodes.add_nodes_from(data_ids)
		nodes2.add_nodes_from(data_indexes)
		nodes2.add_node("__top")
		nodes2.add_node("__bottom")

		position = dict()
		position2 = dict()
		position.update((element, (i, 10)) for i, element in enumerate(data_ids))
		position2.update((element, (i, 20)) for i, element in enumerate(data_indexes))

		axes = plt.axes([0.0, 0.0, 1.0, 1.0])

		node_size = [*self.__generate_size(snapshot)]
		node_size2 = [*[0.0 for i in data_range], 0.0, 0.0]

		index_correction = min(30.0, max(node_size)/750.0)
		position2["__top"] = (-1, -30+index_correction)
		position2["__bottom"] = (len(data_ids), 60-index_correction)

		colors = list()
		colors2 = list()
		for i in data_range:
			colors.append(snapshot.highlights[i])
		for i in data_range:
			colors2.append('w')
		colors2.append('w')
		colors2.append('w')

		labels = dict()
		labels2 = dict()
		labels2["__top"] = ""
		labels2["__bottom"] = ""
		for i in data_range:
			labels[i] = snapshot.data[i]
			labels2["index_%i" % i] = "%i." % i

		nx.draw(nodes, labels=labels, pos=position, with_labels=True, node_size=node_size, ax=axes, node_color=colors, font_color='#00000f')
		nx.draw(nodes2, labels=labels2, pos=position2, with_labels=True, node_size=node_size2, ax=axes, node_color=colors2, font_color='#cccccc', font_weight='bold')
		self.figure.set_facecolor("#00000F")
		self.canvas.draw_idle()

	@staticmethod
	def __generate_size(snapshot: Snapshot) -> list:
		"""
		Wygenerowanie rozmiarów węzłów w zależności od rozmiaru.

		Parametry:
		snapshot - aktualny stan algorytmu. Obiekt typu Snapshot.

		Typ zwracany:
		list
		"""
		only_numbers = True
		for element in snapshot.data:
			if not element.isdigit():
				only_numbers = False
				break

		data = list()
		if not only_numbers:
			data = [len(snapshot.data[i]) + 1 for i in range(len(snapshot.data))]
		else:
			data = [math.log10(abs(float(snapshot.data[i])) + 1) + 1 for i in range(len(snapshot.data))]

		return [500.0 + 60.0 * element ** 2 for element in data]
