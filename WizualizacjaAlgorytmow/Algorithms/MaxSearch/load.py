from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot


class MaxSearch(BasicAlgorithm):
	"""
	Klasa reprezentująca algorytm wyszukiwania maximum w tablicy

	Przykład:
	>>> max_search = MaxSearch()
	"""

	def __init__(self):
		super().__init__("MaxSearch", "Wyszukiwanie wartosci maksymalnej")

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		current_max = self.data[0]
		current_max_index = 0
		self.save_snapshot("Na początek ustalamy najmniejszy element na pierwszą wartość z tablicy (%s)." % current_max,
							{current_max_index: Snapshot.color_current})
		for i in range(1, len(self.data)):
			self.save_snapshot(
				"Porównujemy o wartości '%s' z tablicy z aktualnym minimum (%s)." % (self.data[i], current_max),
				{current_max_index: Snapshot.color_current, i: Snapshot.color_selected})
			if compare(self.data[i], current_max, Comparator.is_greater_than):
				self.save_snapshot("'%s' jest mniejsze od '%s', więc zapamiętujemy nową wartosć minimalną." % (
					self.data[i], current_max), {i: Snapshot.color_current, current_max_index: Snapshot.color_selected})
				current_max = self.data[i]
				current_max_index = i
			else:
				self.save_snapshot(
					"%s nie jest mniejsze od '%s', więc przechodzimy dalej." % (self.data[i], current_max),
					{current_max_index: Snapshot.color_current, i: Snapshot.color_selected})
		self.save_snapshot("Znaleziona wartosć minimalna wynosi '%s'." % current_max,
							{current_max_index: Snapshot.color_current_final})


def __init__():
	return MaxSearch()
