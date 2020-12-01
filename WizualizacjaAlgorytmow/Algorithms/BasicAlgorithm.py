import random

from Paths import Paths
from Algorithms.Algorithm import Algorithm
from Snapshot import Snapshot
from Widgets.NetworkXWidget import NetworkXWidget


class BasicAlgorithm(Algorithm):
	"""
	Klasa abstrakcyjna reprezentująca algorytm niezłożony.
	Jest to algorytm, który przechowuje tylko pojedyncze dane elementu.
	Algorytm dziedziczący po tej klasie będzie wykorzystywać bibliotekę NetworkX.
	
	Parametry:
	name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.
	title - pełna nazwa algorytmu. Wyswietlana w aplikacji.
	
	Przykład:
	>>> min_search = BasicAlgorithm("MinSearch", "Wyszukiwanie Minimum")
	"""
	def __init__(self, name: str = "missing", title: str = "missing"):
		super().__init__(name, title)
		self.visualization_widget = NetworkXWidget
		self.load_buttons()
		self.data.clear()
		self.snapshots.clear()
		self.save_snapshot("")  # pusty snapshot zeby wszystko poprawnie dzialalo

	def add_element(self, value: str):
		"""
		Metoda dodająca element o podanej wartości do tablicy danych.

		Parametry:
		value - wartość elementu, który ma zostać dodany.

		Przykład:
		>>> add_element(5)
		>>> add_element("Janek")
		"""
		self.data.append(value.strip())
		self.save_snapshot("Dodanie elementu '%s' do tablicy danych." % value, {len(self.data)-1: Snapshot.color_selected})

	def remove_element(self, value: str) -> bool:
		"""
		Metoda usuwająca pierwszy znaleziony element o podanej wartości z tablicy danych.

		Parametry:
		value - wartość elementu, który ma zostać usunięty.

		Typ zwracany:
		bool - reprezentuje czy element znajdował się w tablicy.

		Przykład:
		>>> remove_element(5)
		"""
		if self.data.count(value) > 0:
			self.data.remove(value)
			self.save_snapshot("Usunięcie elementu '%s' z tablicy danych." % value)
			return True

		self.save_snapshot("W tablicy danych nie znajduje się element o wartości '%s'." % value)
		return False

	def remove_all_elements(self, value: str):
		"""
		Metoda usuwająca wszystkie elementy o podanej wartości z tablicy danych.

		Parametry:
		value - wartość elementów, które mają zostać usunięte.

		Przykład:
		>>> remove_all_elements(5)
		"""
		self.save_snapshot("Rozpoczynamy usuwanie wszystkich elementów z tablicy o wartości '%s'." % value)
		while self.remove_element(value):
			pass
		self.save_snapshot("Usunięto wszystkie elementy o wartości '%s'." % value)

	def clear(self):
		"""
		Metoda usuwająca wszystkie elementy z tablicy i czyszcząca listę kroków.
		"""
		self.data.clear()
		self.snapshots.clear()
		self.save_snapshot("Usunięto wszystko elementy z tablicy danych i wszystkie kroki są ponownie puste.")

	def shuffle(self):
		"""
		Metoda odpowiedzialna za przemieszanie wszystkich elementów.
		"""
		if len(self.data) == 0:
			return

		random.shuffle(self.data)
		self.save_snapshot("Elementy zostały przemieszane!")

	def execute(self):
		"""
		Abstrakcyjna metoda uruchamiająca algorytm.
		"""
		pass

	def load_buttons(self):
		"""
		Metoda wczytująca klawisze odpowiedzialne za manipulację wizualizacją.
		"""
		self.buttons = list()
		self.buttons.append(["Dodaj", lambda: self.add_element(self.last_value), Paths.icon("plus.png"), True])
		self.buttons.append(["Usuń", lambda: self.remove_element(self.last_value), Paths.icon("minus.png"), True])
		self.buttons.append(["Usuń wszystkie", lambda: self.remove_all_elements(self.last_value), Paths.icon("minus.png"), True])
		self.buttons.append(["Wyczyść", lambda: self.clear(), Paths.icon("clear.png"), True])
		self.buttons.append(["Przemieszaj", lambda: self.shuffle(), Paths.icon("shuffle.png"), True])
		self.buttons.append(["Wykonaj algorytm", lambda: self.execute(), Paths.icon("execute.png"), False])
