from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import math
import networkx as nx


class BasicAlgorithmVisualisation(QWidget):
	def __init__(self, widget, snapshots, description_widget):
		super().__init__()
		self.widget = widget
		self.description_widget = description_widget
		self.init_ui()
		self.snapshots = snapshots
		self.current_snapshot_index = 0
		self.update_snapshot()

	def init_ui(self):
		grid = QGridLayout()
		self.setLayout(grid)
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		grid.addWidget(self.canvas, 1, 1, 1, 1)

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def next_snapshot(self):
		self.current_snapshot_index = min(self.current_snapshot_index+1, len(self.snapshots)-1)
		self.update_snapshot()

	def previous_snapshot(self):
		self.current_snapshot_index = max(self.current_snapshot_index-1, 0)
		self.update_snapshot()

	def update_snapshot(self):
		if len(self.snapshots) == 0:
			return

		snapshot = self.snapshots[self.current_snapshot_index]
		self.description_widget.set_text(snapshot.description)
		self.figure.clf()
		Nodes = nx.Graph()
		Nodes.add_nodes_from(snapshot.data)
		position = dict()
		position.update((element, (i, 1)) for i, element in enumerate(snapshot.data))
		ax1 = plt.axes([0.0, 0.0, 1.0, 1.0])
		tmp_color = list()
		for i in range(len(snapshot.data)):
			tmp_color.append(snapshot.highlights[i])

		nx.draw(Nodes, pos=position, with_labels=True, node_size=[500.0+60.0*(math.log10(abs(i)+1)+1)**2 for i in snapshot.data], ax=ax1, node_color=tmp_color)

		self.canvas.draw_idle()
