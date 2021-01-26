import random

from Paths import Paths
from AlgorithmsLogic.Algorithm import Algorithm
from Settings import Settings
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

	def random_data(self):
		"""
		Metoda dodająca losowe wartości z ustalonego przedziału.
		"""
		amount_of_elements = max(0, min(Settings.input_limit[0]-len(self.data), Settings.random_data_amount[0]))

		if amount_of_elements == 0:
			self.save_snapshot("Nie można dodać więcej elementów! Musisz zwiększyć limit w ustawieniach.")
			return

		for i in range(amount_of_elements):
			self.on_value_change(str(random.randint(Settings.random_data_minimum_value[0], Settings.random_data_maximum_value[0])))
			self.push_back()

	def load_controls(self):
		"""
		Metoda tworząca klawisze oraz pola tekstowe odpowiedzialne za manipulację wizualizacją.
		"""
		self.add_textbox("Wartość elementu:", self.on_value_change, hint="Tutaj możesz wpisać dowolną wartość.")
		self.add_button("Push back", self.push_back, icon=Paths.icon("plus.png"), hint="Dodanie nowego elementu na koniec listy.")
		self.add_button("Push front", self.push_front, icon=Paths.icon("plus.png"), hint="Dodanie nowego elementu na początek listy.")
		self.add_button("Pop back", self.pop_back, icon=Paths.icon("minus.png"), hint="Pobranie i usunięcie elementu z końca listy.")
		self.add_button("Pop front", self.pop_front, icon=Paths.icon("minus.png"), hint="Pobranie i usunięcie elementu z początku listyy.")
		self.add_button("Usuń", self.remove, icon=Paths.icon("minus.png"), hint="Usunięcie pierwszego napotkanego elementu o podanej wartości.")
		self.add_button("Wyczyść", self.clear, icon=Paths.icon("clear.png"), hint="Usunięcie wszystkich elementów oraz przywrócenie stanu początkowego.")
		self.add_button("Losowe dane", self.random_data, icon=Paths.icon("random.png"), hint="Wylosowanie danych z ustawionego przedziału.")
