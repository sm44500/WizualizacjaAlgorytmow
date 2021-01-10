import math

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtCore import Qt

from Snapshot import Snapshot
from Styles import Styles
from Widgets.BaseWidget import BaseWidget


class NetworkXWidget(BaseWidget):
	"""
	Widget wizualuzacji opartej na bibliotece NetworkX.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QGridLayout)
		self.figure = None
		self.canvas = None
		self.background_color = '#00000f'
		self.node_text_color = self.background_color
		self.index_text_color = '#cccccc'
		self.label = QLabel(self)
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)

		self.setStyleSheet(Styles.description_background)

		self.render_snapshot(Snapshot([], "", {}))

	def render_snapshot(self, snapshot: Snapshot):
		"""
		Wyświetla aktualny stan algorytmu.

		Parametry:
		snapshot - aktualny stan algorytmu. Obiekt typu Snapshot.
		"""
		self.clean_figure()

		if len(snapshot.data) > 0:
			self.widget_layout.addWidget(self.canvas)
			data_range = range(len(snapshot.data))
			axes = plt.axes([0.0, 0.0, 1.0, 1.0])
			self.render_nodes(snapshot, axes)
			self.render_indexes(data_range, axes)
		else:
			self.widget_layout.addWidget(self.label)
			self.render_hint()

		self.render_figure()

	def clean_figure(self):
		"""
		Wyczyszczenie poprzedniej wizualizacji.
		"""
		self.figure.clf()
		self.widget_layout.removeWidget(self.label)
		self.widget_layout.removeWidget(self.canvas)

	def render_figure(self):
		"""
		Wyrysowanie wizualizacji.
		"""
		self.figure.set_facecolor(self.background_color)
		self.canvas.draw_idle()

	def render_nodes(self, snapshot: Snapshot, axes):
		"""
		Wyrysowanie aktualnego kroku.

		Parametry:
		snapshot - obiekt reprezentujacy aktualny krok.
		axes - proporcje tekstury na jakiej mają zostać wyrysowane.
		"""
		data_range = range(len(snapshot.data))
		data_ids = [data_id for data_id in data_range]

		nodes = nx.Graph()
		nodes.add_nodes_from(data_ids)

		positions = dict()
		positions.update((element, (i, 10)) for i, element in enumerate(data_ids))

		colors = list()
		for i in data_range:
			colors.append(snapshot.highlights[i])

		labels = dict()
		for i in data_range:
			labels[i] = snapshot.data[i]

		nx.draw(nodes, labels=labels, pos=positions, with_labels=True, node_shape='s', node_size=self.__generate_node_sizes(snapshot),
				ax=axes, node_color=colors, font_color=self.node_text_color)

	def render_indexes(self, data_range: range, axes):
		"""
		Wyrysowanie indeksów nad istniejącymi obiektami.

		Parametry:
		data_range - przedział indeksów jakie mają zostać wyrysowane.
		axes - proporcje tekstury na jakiej mają zostać wyrysowane.
		"""
		data_indexes = ["index_%i" % index for index in data_range]

		nodes = nx.Graph()
		nodes.add_nodes_from(data_indexes)
		nodes.add_node("__top")
		nodes.add_node("__bottom")

		positions = dict()
		positions.update((element, (i, 20)) for i, element in enumerate(data_indexes))

		node_sizes = [*[0.0 for i in data_range], 0.0, 0.0]

		index_correction = min(30.0, max(node_sizes)/750.0)
		positions["__top"] = (-1, -30+index_correction)
		positions["__bottom"] = (len(data_indexes), 60-index_correction)

		colors = list(['w', 'w'])
		for i in data_range:
			colors.append('w')

		labels = dict()
		labels["__top"] = ""
		labels["__bottom"] = ""
		for i in data_range:
			labels["index_%i" % i] = "%i." % i

		nx.draw(nodes, labels=labels, pos=positions, with_labels=True, node_size=node_sizes, ax=axes,
				node_color=colors, font_color=self.index_text_color, font_weight='bold')

	def render_hint(self):
		"""
		Wyświetlenie podpowiedzi dla użytkownika, gdy nie wprowadzono żadnych danych.
		"""
		self.label.setText("")
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setStyleSheet("""background-color:%s; color:%s; font-family:Arial; font-size:20px; font-weight: bold;""" %
								(self.background_color, self.index_text_color))

	@staticmethod
	def __generate_node_sizes(snapshot: Snapshot) -> list:
		"""
		Wygenerowanie rozmiarów węzłów w zależności od rozmiaru tekstu.

		Parametry:
		snapshot - aktualny stan algorytmu. Obiekt typu Snapshot.

		Powrót:
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
