from Paths import Paths
from Algorithms.Algorithm import Algorithm
from Snapshot import Snapshot
from Widgets.NodeZWidget import NodeZWidget


class AdvancedAlgorithm(Algorithm):
	"""
	Klasa abstrakcyjna reprezentująca algorytm złożony.
	Jest to algorytm, który przechowuje elementy typy Node.
	Algorytm dziedziczący po tej klasie będzie wykorzystywać bibliotekę NodeZ.

	Parametry:
	name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.
	title - pełna nazwa algorytmu. Wyswietlana w aplikacji.

	Przykład:
	>>> singly_linked_list = AdvancedAlgorithm("SinglyLinkedList", "Lista jednokierunkowa")
	"""

	def __init__(self, name: str = "missing", title: str = "missing"):
		super().__init__(name, title)
		self.visualization_widget = NodeZWidget
		self.load_buttons()
		self.data.clear()
		self.snapshots.clear()

	def head(self):
		pass

	def tail(self):
		pass

	def push_front(self, value: str):
		pass

	def push_back(self, value: str):
		pass

	def pop_front(self, value: str):
		pass

	def pop_back(self, value: str):
		pass

	def remove(self, value: str):
		pass

	def clear(self):
		"""
		Metoda usuwająca wszystkie elementy z tablicy i czyszcząca listę kroków.
		"""
		self.data.clear()
		self.snapshots.clear()
		self.save_snapshot("Usunięto wszystko elementy z tablicy danych i wszystkie kroki są ponownie puste.")

	def load_buttons(self):
		"""
		Metoda wczytująca klawisze odpowiedzialne za manipulację wizualizacją.
		"""
		self.buttons = list()