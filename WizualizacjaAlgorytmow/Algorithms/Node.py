class Node:
	def __init__(self, value, next_node=None, previous_node=None):
		self.value = value
		self.next_node = next_node
		self.previous_node = previous_node