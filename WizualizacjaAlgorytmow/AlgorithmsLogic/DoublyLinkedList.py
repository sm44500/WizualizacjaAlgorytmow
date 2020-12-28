from AlgorithmsLogic.ListAlgorithm import ListAlgorithm
from Widgets.NodZWidget import NodZWidget
from Node import Node

class DoublyListNode(Node):
	"""
	Klasa reprezuntująca węzeł listy dwukierunkowej

	Przykład:
		>>> doubly_linked_list_node = DoublyLinkedNode()
	"""
	number = 0
	def __init__(self):
		super().__init__("Node %s" % DoublyListNode.number)
		DoublyListNode.number+=1
		self.next = None
		self.previous = None
		self.next_attr = self.add_attribute("Next")
		self.previous_attr = self.add_attribute("Previous")
		self.data_attr = self.add_attribute("Dane: ")

class DoublyLinkedList(ListAlgorithm):
	"""
	Klasa reprezentująca listę dwukierunkową

	Przykład:
		>>> doubly_linked_list = DoublyLinkedList()
	"""

	def __init__(self):
		super().__init__("DoublyLinkedList", "Lista dwukierunkowa")
		self.difficulty = 3
		self.head = None
		self.tail = None

	def push_back(self):
		"""
		Metoda dodająca element na końcu listy
		"""
		value = self.textbox_value
		node = DoublyListNode()
		node.data_attr.name = "Dane: " + value

		if self.head is None:
			self.head = node
		else:
			last_node = self.head
			while not last_node.next is None:
				last_node = last_node.next

			last_node.next = node
			node.previous = last_node

			last_node.next_attr.connection = node.next_attr
			node.previous_attr.connection = last_node.previous_attr

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
		else:
			tmp = self.head
			self.head = node
			self.head.next = tmp
			self.head.next_attr.connection = tmp.next_attr
			tmp.previous = self.head
			tmp.previous_attr.connection = self.head.previous_attr

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

			self.head.previous = None
			self.head.previous_attr = None

			DoublyListNode.number -= 1
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
				tmp = self.tail
				self.tail = current
				self.tail.next = None
				self.tail.next_attr = None
				DoublyListNode.number -= 1
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
			while current.next != None:
				if current.next.data_attr == value:
					current.next = current.next.next
					current.next_attr.connection = current.next.next_attr

					current.next.previous = current
					current.next.previous_attr.connection = current.previous_attr
					break
				current = current.next

			current.next_attr.connection = current.next_attr

		DoublyListNode.number -= 1
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
