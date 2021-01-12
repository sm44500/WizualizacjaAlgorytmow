from Snapshot import Snapshot
from AlgorithmsLogic.ListAlgorithm import ListAlgorithm
from Widgets.NodZWidget import NodZWidget
from Node import Node

class SinglyListNode(Node):
	"""
	Klasa reprezuntująca węzeł listy jednokierunkowej

	Przykład:
		>>> singly_linked_list_node = SinglyLinkedNode()
	"""
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
		super().__init__("SinglyLinkedList", "Lista jednokierunkowa")
		self.difficulty = 2
		self.head = None

	def push_back(self):
		"""
		Metoda dodająca element na końcu listy
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + str(value)

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

	def push_front(self):
		"""
		Metoda dodająca element na początku listy
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + str(value)

		if self.head is None:
			self.head = node
		else:
			tmp = self.head
			self.head = node
			self.head.next = tmp
			self.head.next_attr.connection = tmp.next_attr
		self.data.insert(0, node)
		self.save_snapshot("Zakończono dodawanie elementu")

	def pop_front(self):
		"""
		Metoda usuwająca element na początku listy
		"""
		if self.head != None:
			tmp = self.head
			self.head = self.head.next
			self.head.next_attr.connection = tmp.next.next_attr
			SinglyListNode.number -= 1
			self.data = self.data[1:]
			self.save_snapshot("Zakończono usunięcie elementu")
			return tmp

	def pop_back(self):
		"""
		Metoda usuwająca element na końcu listy
		"""
		if self.head != None:
			current = self.head
			if len(self.data) > 1:
				while current.next != None:
					if current.next.next == None:
						result = current.next
						current.next = None
						current.next_attr.connection = None
						SinglyListNode.number -= 1
						self.data = self.data[:-1]
						return result
					current = current.next
			else:
				result = self.head
				self.clear()
				return result
			self.save_snapshot("Zakończono usunięcie elementu")

	def remove(self):
		"""
		Metoda usuwająca element o wskazanej wartości
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + str(value)

		if self.head is None:
			self.save_snapshot("Usunięcie elementu nie powiodło się: lista jest pusta")
		else:
			current = self.head
			while current.next != None:
				if current.next.data_attr == value:
					current.next = current.next.next
					current.next_attr.connection = current.next.next_attr
					break
				current = current.next

			current.next_attr.connection = current.next_attr

		SinglyListNode.number -= 1
		self.data.remove(node)
		self.save_snapshot("Zakończono usunięcie elementu")

	def head(self):
		"""
		Metoda zwracająca głowę listy jednokierunkowej
		"""
		return self.head

	def tail(self):
		"""
		Metoda zwracająca ogon listy jednokierunkowej
		"""
		return self.data[-1]
