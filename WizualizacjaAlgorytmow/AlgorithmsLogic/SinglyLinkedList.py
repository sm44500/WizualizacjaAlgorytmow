from AlgorithmsLogic.ListAlgorithm import ListAlgorithm
from Widgets.NodZWidget import NodZWidget
from Node import Node

class SinglyListNode(Node):
	number = 0
	def __init__(self):
		super().__init__("Node %s" % SinglyListNode.number)
		SinglyListNode.number+=1
		self.next = None
		self.next_attr = self.add_attribute("Next")
		self.data_attr = self.add_attribute("Dane: ")

class SinglyLinkedList(ListAlgorithm):
	"""
	Klasa reprezentująca listę jednokierunkową

	Przykład:
		>>> singly_linked_list = SinglyLinkedList()
	"""

	def __init__(self):
		super().__init__("SinglyLinkedList", "TODO: Lista jednokierunkowa")
		self.difficulty = 2
		self.head = None

	def push_back(self):
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + value

		if self.head is None:
			self.head = node
		else:
			last_node = self.head
			while not last_node.next is None:
				last_node = last_node.next

			last_node.next = node
			last_node.next_attr.connection = node.next_attr

		self.data.append(node)
		self.save_snapshot("Zakończono dodawanie elementu")

