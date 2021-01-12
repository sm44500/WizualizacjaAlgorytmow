from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtCore import QPointF

from Snapshot import Snapshot
from Node import Node
from Widgets.BaseWidget import BaseWidget
import NodZ.Main as nodz_main

class NodZWidget(BaseWidget):
	"""
	Widget wizualizacji opartej na bibliotece NodZ.

	Parametry:
		parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QGridLayout)
		self.nodz_nodes = []
		self.nodz = None
		self.setup_ui()

		self.render_snapshot(
			Snapshot([],"Test",[])
		)

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.nodz = nodz_main.Nodz(None)
		self.nodz.initialize()
		self.widget_layout.addWidget(self.nodz)
		self.nodz.show()
		self.nodz.scale(0.6, 0.6)
		pass

	def create_node(self, name, preset, position=None):
		node = self.nodz.createNode(name=name, preset=preset, position=position)
		return node

	def create_attribute(self, node, name, preset):
		node_attr = self.nodz.createAttribute(
			node=node,
			name=name,
			index=-1,
			preset=preset,
			plug=True,
			socket=True,
			dataType=str,
			plugMaxConnections=1,
			socketMaxConnections=1
		)
		return node_attr

	def render_snapshot(self, snapshot: Snapshot):
		self.nodz.clearGraph()
		nodes = snapshot.data
		center_position = self.nodz.mapToScene(self.nodz.viewport().rect().center())
		highlights = snapshot.highlights

		for index, node in enumerate(nodes):
			#TODO calculate pos
			node_pos = QPointF(center_position)
			node_pos.setX(((center_position.x() * 2) / len(nodes)) * (index + 1) - 200)

			if highlights[index] == Snapshot.color_idle:
				attr_preset = 'attr_color_idle'
				node_preset = 'node_color_idle'
			elif highlights[index] == Snapshot.color_selected:
				attr_preset = 'attr_color_selected'
				node_preset = 'node_color_selected'
			elif highlights[index] == Snapshot.color_current:
				attr_preset = 'attr_color_current'
				node_preset = 'node_color_current'
			elif highlights[index] == Snapshot.color_current_final:
				attr_preset = 'attr_color_current_final'
				node_preset = 'node_color_current_final'

			nodz_node = self.create_node(node.name, preset=node_preset, position=node_pos)
			for attr in node.attributes:
				nodz_attr = self.create_attribute(nodz_node, attr.name, attr_preset)
			self.nodz_nodes.append(nodz_node)

		for node in nodes:
			for attr in node.attributes:
				if (not attr.connection is None) and (attr.node_name != attr.connection.node_name):
					self.nodz.createConnection(
						attr.node_name, attr.name,
						attr.connection.node_name, attr.connection.name
					)

		self.nodz.evaluateGraph()
		pass
		