class Node:
	"""
	Obiekt reprezentujący węzeł wizualizacji nodz.

	Parametry:
		name - nazwa węzła

	Przykład:
		>>>node1 = Node("Node 1")
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
	"""
	def __init__(self, name):
		self.name = name
		self.attributes = []

	def add_attribute(self, name):
		"""
		Dodaje wpis do węzła.

		Parametry:
		name - nazwa parametru.
		"""
		attribute = NodeAttribute(name, self.name)
		self.attributes.append(attribute)
		return attribute

class NodeAttribute:
	"""
	Obiekt reprezentujący atrybut węzła.
	"""
	def __init__(self, name, node_name):
		self.node_name = node_name
		self.name = name
		self.connection = None