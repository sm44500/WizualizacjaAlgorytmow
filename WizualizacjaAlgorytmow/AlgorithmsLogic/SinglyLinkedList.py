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

		self.save_snapshot("Sprawdzamy czy lista posiada głowę (head).")
		if not len(self.data):
			self.head = node
			self.save_snapshot("Lista nie posiada głowy, więc dodawany element nią zostaje.")
		else:
			last_node = self.head
			while not last_node.next is None:
				last_node = last_node.next

			last_node.next = node
			last_node.next_attr.connection = node.next_attr

		self.data.append(node)
		self.save_snapshot("Zakończono dodawanie elementu", {int(node.number)-1: Snapshot.color_current_final})

	def push_front(self):
		"""
		Metoda dodająca element na początku listy
		"""
		value = self.textbox_value
		node = SinglyListNode()
		node.data_attr.name = "Dane: " + str(value)

		self.save_snapshot("Sprawdzamy czy lista posiada głowę (head).")
		if not len(self.data):
			self.head = node
			self.save_snapshot("Lista nie posiada głowy, więc dodawany element nią zostaje.")
		else:
			tmp = self.head
			self.head = node
			self.head.next = tmp
			self.head.next_attr.connection = tmp.next_attr
		self.data.insert(0, node)
		self.save_snapshot("Zakończono dodawanie elementu", {int(node.number)-1: Snapshot.color_current_final})

	def pop_front(self):
		"""
		Metoda usuwająca element na początku listy
		"""
		if len(self.data):
			if len(self.data) > 1:
				self.head = self.head.next
				self.data = self.data[1:]
				self.save_snapshot("Zakończono usunięcie elementu")
			else:
				self.clear()
				self.head = 0
		else:
			self.save_snapshot("Usunięcie elementu nie powiodło się: lista jest pusta")

	def pop_back(self):
		"""
		Metoda usuwająca element na końcu listy
		"""
		if len(self.data):
			current = self.head
			if len(self.data) > 1:
				while current.next != None:
					if current.next.next == None:
						current.next = None
						current.next_attr.connection = None
						self.data = self.data[:-1]
					else:
						current = current.next
			else:
				self.clear()
				self.head = None
			self.save_snapshot("Zakończono usunięcie elementu")
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
						self.data[i - 1].next = self.data[i + 1] if i + 1 < len(self.data) else None
						self.data[i - 1].next_attr.connection = self.data[i + 1].next_attr if i + 1 < len(self.data) else None
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
		return self.data[-1]
