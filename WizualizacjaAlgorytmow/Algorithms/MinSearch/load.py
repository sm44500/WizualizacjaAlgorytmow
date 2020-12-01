from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot


class MinSearch(BasicAlgorithm):
	"""
	Klasa reprezentująca algorytm wyszukiwania minimum w tablicy

	Przykład:
	>>> min_search = MinSearch()
	"""

	def __init__(self):
		super().__init__("MinSearch", "Wyszukiwanie wartości minimalnej")
		self.difficulty = 1

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		current_min = self.data[0]
		current_min_index = 0
		self.save_snapshot("Na początek ustalamy najmniejszy element na pierwszą wartość z tablicy równą '%s'." % current_min,
							{current_min_index: Snapshot.color_current})
		for i in range(1, len(self.data)):
			self.save_snapshot(
				"Porównujemy %s. element z tablicy o wartości '%s' z aktualnym minimum wynoszącym '%s'." % (i, self.data[i], current_min),
				{current_min_index: Snapshot.color_current, i: Snapshot.color_selected})
			if compare(self.data[i], current_min, Comparator.is_less_than):
				self.save_snapshot("'%s' jest mniejsze od '%s', więc zapamiętujemy nową wartosć minimalną." % (
				self.data[i], current_min), {i: Snapshot.color_current, current_min_index: Snapshot.color_selected})
				current_min = self.data[i]
				current_min_index = i
			else:
				self.save_snapshot(
					"'%s' nie jest mniejsze od '%s', więc przechodzimy dalej." % (self.data[i], current_min),
					{current_min_index: Snapshot.color_current, i: Snapshot.color_selected})
		self.save_snapshot("Był to ostatni element z tablicy danych, więc algorytm kończy działanie.", {current_min_index: Snapshot.color_selected})
		self.save_snapshot("Znaleziona wartosć minimalna wynosi '%s'." % current_min,
							{current_min_index: Snapshot.color_current_final})


def __init__():
	return MinSearch()
