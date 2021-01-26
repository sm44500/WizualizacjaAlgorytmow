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
		node.data_attr.name = "Dane: " + str(value)

		if not len(self.data):
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
		self.save_snapshot("Zakończono dodawanie elementu.")

	def push_front(self):
		"""
		Metoda dodająca element na początku listy
		"""
		value = self.textbox_value
		node = DoublyListNode()
		node.data_attr.name = "Dane: " + str(value)

		if not len(self.data):
			self.head = node
		else:
			tmp = self.head
			self.head = node
			self.head.next = tmp
			self.head.next_attr.connection = tmp.next_attr
			tmp.previous = self.head
			tmp.previous_attr.connection = self.head.previous_attr

		self.data.insert(0, node)
		self.save_snapshot("Zakończono dodawanie elementu.")

	def pop_front(self):
		"""
		Metoda usuwająca element na początku listy
		"""
		if len(self.data):
			if len(self.data) > 1:
				self.head = self.head.next

				self.head.previous = None
				self.head.previous_attr.connection = None

				self.data = self.data[1:]
				self.save_snapshot("Zakończono usunięcie elementu.")
			else:
				self.clear()
		else:
			self.save_snapshot("Usuwanie elementu nie powiodło się, ponieważ lista jest pusta.")

	def pop_back(self):
		"""
		Metoda usuwająca element na końcu listy
		"""
		if len(self.data):
			current = self.head
			if len(self.data) > 1:
				self.tail = self.data[-2]
				self.tail.next = None
				self.tail.next_attr.connection = None
				self.data = self.data[:-1]
			else:
				self.clear()
			self.save_snapshot("Zakończono usuwanie elementu.")
		else:
			self.save_snapshot("Usuwanie elementu nie powiodło się, ponieważ lista jest pusta.")

	def remove(self):
		"""
		Metoda usuwająca element o wskazanej wartości
		"""
		value = self.textbox_value
		node = DoublyListNode()
		node.data_attr.name = "Dane: " + str(value)

		if not len(self.data):
			self.save_snapshot("Usuwanie elementu nie powiodło się, ponieważ lista jest pusta.")
		else:
			removed = False
			current = self.head
			if current.data_attr.name == node.data_attr.name:
				self.pop_front()
			else:
				for i in range(len(self.data)):
					if self.data[i].data_attr.name == node.data_attr.name:
						self.data[i - 1].next = self.data[i + 1] if i + 1 < len(self.data) else None
						self.data[i - 1].next_attr.connection = self.data[i + 1].next_attr if i + 1 < len(self.data) else None

						if i + 1 < len(self.data):
							self.data[i + 1].previous = self.data[i - 1]
							self.data[i + 1].previous_attr.connection = self.data[i - 1].previous_attr
						self.data.remove(self.data[i])
						removed = True
						self.save_snapshot("Zakończono usunięcie elementu.")
						break
					if i == len(self.data) - 1 and not removed:
						self.save_snapshot("Usunięcie elementu nie powiodło się, ponieważ nie ma węzła z takimi danymi.")


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
