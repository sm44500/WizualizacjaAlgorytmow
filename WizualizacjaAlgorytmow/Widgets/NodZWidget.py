from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtCore import QPointF

from Snapshot import Snapshot
from Widgets.BaseWidget import BaseWidget
import NodZ.Main as nodz_main
import uuid

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

	def create_node(self, name, position=None):
		node = self.nodz.createNode(name=name, preset='node_preset_1', position=position)
		return node

	def create_attribute(self, node, name):
		node_attr = self.nodz.createAttribute(
			node=node,
			name=name,
			index=-1,
			preset='attr_preset_1',
			plug=True,
			socket=True,
			dataType=str,
			plugMaxConnections=1,
			socketMaxConnections=1
		)
		return node_attr

	def render_snapshot(self, snapshot: Snapshot):
		node1 = Node("Node 1")
		attr1 = node1.add_attribute("Attr 1")
		attr2 = node1.add_attribute("Attr 2")
		attr3 = node1.add_attribute("Attr 3")

		node2 = Node("Node 2")
		attr4 = node2.add_attribute("Attr 4")
		attr5 = node2.add_attribute("Attr 5")
		attr6 = node2.add_attribute("Attr 6")

		attr1.connection = attr5
		attr2.connection = attr6
		attr3.connection = attr4

		node3 = Node("Node 3")
		node4 = Node("Node 4")
		node5 = Node("Node 5")
		
		self.nodz.clearGraph()
		self.nodz_nodes = []

		nodes = [node1, node2, node3, node4, node5]

		center_position = self.nodz.mapToScene(self.nodz.viewport().rect().center())

		for index, node in enumerate(nodes):
			#TODO calculate pos
			node_pos = QPointF(center_position)
			node_pos.setX( ((center_position.x() * 2) / len(nodes)) * (index + 1) )
			nodz_node = self.create_node(node.name, position=node_pos)
			for attr in node.attributes:
				nodz_attr = self.create_attribute(nodz_node, attr.name)
				#TODO highlight attr etc

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

class Node:
	def __init__(self, name):
		self.name = name
		self.attributes = []

	def add_attribute(self, name):
		attribute = NodeAttribute(name, self.name)
		self.attributes.append(attribute)
		return attribute

class NodeAttribute:
	def __init__(self, name, node_name):
		self.node_name = node_name
		self.name = name
		self.connection = None
		