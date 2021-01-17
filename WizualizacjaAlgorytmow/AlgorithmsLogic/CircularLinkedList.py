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
		node.data_attr.name = "Dane: " + str(value)

		if not len(self.data):
			self.head = node
			self.tail = self.head
			self.head.next = self.tail
			self.head.next_attr.connection = self.tail.next_attr
		else:
			self.tail.next = node
			self.tail.next_attr.connection = node.next_attr
			self.tail = node
			self.tail.next = self.head
			self.tail.next_attr.connection = self.head.next_attr

		self.data.append(node)
		self.save_snapshot("Zakończono dodawanie elementu")

	def push_front(self):
		"""
		Metoda dodająca element na początku listy
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + str(value)

		if not len(self.data):
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
		if len(self.data):
			if len(self.data) > 1:
				self.head = self.head.next
				self.data = self.data[1:]
				self.tail.next = self.head
				self.tail.next_attr.connection = self.head.next_attr
				self.save_snapshot("Zakończono usunięcie elementu")
			else:
				self.clear()
		else:
			self.save_snapshot("Usunięcie elementu nie powiodło się: lista jest pusta")

	def pop_back(self):
		"""
		Metoda usuwająca element na końcu listy
		"""
		if len(self.data):
			if len(self.data) > 1:
				self.tail = self.data[-2]
				self.tail.next = self.head
				self.tail.next_attr.connection = self.head.next_attr
				self.data = self.data[:-1]

				self.save_snapshot("Zakończono usunięcie elementu")
			else:
				self.clear()
		else:
			self.save_snapshot("Usunięcie elementu nie powiodło się: lista jest pusta")

	def remove(self):
		"""
		Metoda usuwająca element o wskazanej wartości
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + str(value)
		if not len(self.data):
			self.save_snapshot("Usunięcie elementu nie powiodło się: lista jest pusta")
		else:
			current = self.head
			if current.data_attr.name == node.data_attr.name:
				self.pop_front()
			else:
				removed = False
				for i in range(len(self.data)):
					if self.data[i].data_attr.name == node.data_attr.name:
						if i == 0:
							self.clear()
							break
						self.data[i - 1].next = self.data[i + 1] if i + 1 < len(self.data) else self.head
						self.data[i - 1].next_attr.connection = self.data[i + 1].next_attr if i + 1 < len(self.data) else self.head.next_attr
						if i == len(self.data) - 1:
							self.tail = self.data[i - 1]
						self.data.remove(self.data[i])
						removed = True
						self.save_snapshot("Zakończono usunięcie elementu")
						break
					if i == len(self.data) - 1 and not removed:
						self.save_snapshot("Usunięcie elementu nie powiodło się: nie ma węzła z takimi danymi")

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
