from Paths import Paths
from AlgorithmsLogic.Algorithm import Algorithm
from Snapshot import Snapshot
from Widgets.NodZWidget import NodZWidget


class ListAlgorithm(Algorithm):
	"""
	Klasa abstrakcyjna reprezentująca algorytm złożony.
	Jest to algorytm, który przechowuje elementy typu Node.
	Algorytm dziedziczący po tej klasie będzie wykorzystywać bibliotekę NodZ.

	Parametry:
		name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.
		title - pełna nazwa algorytmu. Wyswietlana w aplikacji.

	Przykład:
		>>> singly_linked_list = ListAlgorithm("SinglyLinkedList", "Lista jednokierunkowa")
	"""

	def __init__(self, name: str = "missing", title: str = "missing"):
		super().__init__(name, title)
		self.visualization_widget = NodZWidget
		self.load_controls()
		self.data.clear()
		self.snapshots.clear()

	def head(self):
		pass

	def tail(self):
		pass

	def push_front(self):
		pass

	def push_back(self):
		pass

	def pop_front(self):
		pass

	def pop_back(self):
		pass

	def remove(self):
		pass

	def clear(self):
		"""
		Metoda usuwająca wszystkie elementy z tablicy i czyszcząca listę kroków.
		"""
		self.data.clear()
		self.snapshots.clear()
		self.save_snapshot("Usunięto wszystko elementy z tablicy danych i wszystkie kroki są ponownie puste.")

	def on_value_change(self, new_value):
		self.textbox_value = new_value

	def load_controls(self):
		"""
		Metoda tworząca klawisze oraz pola tekstowe odpowiedzialne za manipulację wizualizacją.
		"""
		self.add_textbox("Wartość elementu:", self.on_value_change, hint="Tutaj możesz wpisać dowolną wartość.")
		self.add_button("Dodaj", self.push_back, icon=Paths.icon("plus.png"), hint="Dodanie nowego elementu na koniec tablicy.")