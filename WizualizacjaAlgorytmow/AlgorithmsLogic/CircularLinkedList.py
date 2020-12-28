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

class CircularLinkedList(ListAlgorithm):
	"""
	Klasa reprezentująca listę dwukierunkową

	Przykład:
		>>> circular_linked_list = CircularLinkedList()
	"""

	def __init__(self):
		super().__init__("CircularLinkedList", "Lista cykliczna")
		self.difficulty = 3
		self.head = None
		self.tail = None

	def push_back(self):
		"""
		Metoda dodająca element na końcu listy
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + value

		if self.head is None:
			self.head = node
			self.tail = self.head
			self.head.next = self.tail
			self.head.next_attr.connection = self.tail.next_attr
		else:
			last_node = self.head
			while last_node.next != self.head:
				last_node = last_node.next

			last_node.next = node
			last_node.next_attr.connection = node.next_attr
			node.next = self.head
			node.next_attr.connection = self.head.next_attr
			self.tail = node

		self.data.append(node)
		self.save_snapshot("Zakończono dodawanie elementu")

	def push_front(self):
		"""
		Metoda dodająca element na początku listy
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + value

		if self.head is None:
			self.head = node
			self.tail = self.head
			self.head.next = self.tail
			self.head.next_attr.connection = self.tail.next_attr
		else:
			tmp = self.head
			self.head = node
			self.head.next = tmp
			self.head.next_attr.connection = tmp.next_attr

			self.tail.next = self.head
			self.tail.next_attr.connection = self.head.next_attr
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

			self.tail.next = self.head
			self.tail.next_attr.connection = self.head.next_attr

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
				while current.next != self.tail:
					current = current.next
				self.tail = current
				self.tail.next = self.head
				self.tail.next_attr.connection = self.head.next_attr

				SinglyListNode.number -= 1
				self.data = self.data[:-1]
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
		node.data_attr.name = "Dane: " + value

		if self.head is None:
			self.save_snapshot("Usunięcie elementu nie powiodło się: lista jest pusta")
		else:
			current = self.head
			while current.next != self.head:
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
		return self.tail
