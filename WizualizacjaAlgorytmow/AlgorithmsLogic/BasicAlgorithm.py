import random

from Paths import Paths
from AlgorithmsLogic.Algorithm import Algorithm
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
		self.load_controls()
		self.data.clear()
		self.last_value = ""
		self.snapshots.clear()

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
		self.save_snapshot("Dodanie elementu '%s'." % value, {len(self.data) - 1: Snapshot.color_selected})

	def remove_element(self, value: str) -> bool:
		"""
		Metoda usuwająca pierwszy znaleziony element o podanej wartości z tablicy danych.

		Parametry:
			value - wartość elementu, który ma zostać usunięty.

		Powrót:
			bool - reprezentuje czy element znajdował się w tablicy.

		Przykład:
			>>> remove_element(5)
		"""
		if self.data.count(value) > 0:
			self.data.remove(value)
			self.save_snapshot("Usunięcie elementu '%s'." % value)
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
		self.save_snapshot("Usunięto wszystko elementy i wyczyszczono kroki.")

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

	def random_data(self):
		"""
		Metoda doająca n losowych wartości z przedziału <0;100>.
		Jeżeli w pole tekstowe nie zostało wpisane nic lub tekst -> n=10
		Jeżeli w pole tekstowe została wpisana liczba -> n=ta liczba
		"""
		if self.last_value == '' or not self.last_value.isdigit():
			n = 10
		else:
			n = int(self.last_value)
		for i in range(n):
			self.add_element(str(random.randint(0, 100)))

	def on_value_change(self, new_value):
		self.last_value = new_value

	def load_controls(self):
		"""
		Metoda tworząca klawisze oraz pola tekstowe odpowiedzialne za manipulację wizualizacją.
		"""

		self.add_textbox("Wartość elementu:", self.on_value_change, hint="Tutaj możesz wpisać dowolną wartość.")
		self.add_button("Dodaj", lambda: self.add_element(self.last_value), icon=Paths.icon("plus.png"), hint="Dodanie nowego elementu na koniec tablicy.")
		self.add_button("Usuń", lambda: self.remove_element(self.last_value), icon=Paths.icon("minus.png"), hint="Usunięcie pierwszego napotkanego elementu o podanej wartości.")
		self.add_button("Usuń wszystkie", lambda: self.remove_all_elements(self.last_value), icon=Paths.icon("minus.png"), hint="Usunięcie wszystkich napotkanych elementów o podanej wartości.")
		self.add_button("Wyczyść", self.clear, icon=Paths.icon("clear.png"), hint="Usunięcie wszystkich elementów oraz przywrócenie stanu początkowego.")
		self.add_button("Losowe dane", self.random_data, icon=Paths.icon("random.png"), hint="Wylosowanie danych z ustawionego przedziału.")
		self.add_button("Przemieszaj", self.shuffle, icon=Paths.icon("shuffle.png"), hint="Zamiana kolejności wszystkich elementów w tablicy.")
		self.add_button("Wykonaj algorytm", self.execute, icon=Paths.icon("execute.png"), hint="Rozpoczęcie wykonywania algorytmu.", update=False)

