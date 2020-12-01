from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot


class SimpleSearch(BasicAlgorithm):
	"""
	Klasa reprezentująca algorytm wyszukiwania elementu w tablicy

	Przykład:
	>>> simple_search = SimpleSearch()
	"""

	def __init__(self):
		super().__init__("SimpleSearch", "Wyszukiwanie proste")
		self.difficulty = 1
		self.found = False

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		for i in range(len(self.data)):
			self.save_snapshot(
				"Porównujemy %s. element z tablicy o wartości '%s' z wyszukiwanym elementem '%s'." % (i, self.data[i], self.last_value),
				{i: Snapshot.color_current})
			if self.data[i] == self.last_value:
				self.save_snapshot("Znaleziono element o wartości '%s'" % (self.data[i]), {i: Snapshot.color_current_final})
				self.found = True
				break
			else:
				self.save_snapshot("'%s' nie jest równe '%s', więc przechodzimy dalej." % (self.data[i], self.last_value),{i: Snapshot.color_current})
		if not self.found:
			self.save_snapshot("Wyszukiwany element nie został znaleziony.")


def __init__():
	return SimpleSearch()
