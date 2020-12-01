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
		super().__init__("MaxSearch", "Wyszukiwanie wartości maksymalnej")
		self.difficulty = 1

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		current_max = self.data[0]
		current_max_index = 0
		self.save_snapshot("Na początek ustalamy największy element na pierwszą wartość z tablicy równą '%s'." % current_max,
							{current_max_index: Snapshot.color_current})
		for i in range(1, len(self.data)):
			self.save_snapshot(
				"Porównujemy %s. element z tablicy o wartości '%s' z aktualnym maksimum wynoszącym '%s')." % (i, self.data[i], current_max),
				{current_max_index: Snapshot.color_current, i: Snapshot.color_selected})
			if compare(self.data[i], current_max, Comparator.is_greater_than):
				self.save_snapshot("'%s' jest większe od '%s', więc zapamiętujemy nową wartosć maksymalną." % (
					self.data[i], current_max), {i: Snapshot.color_current, current_max_index: Snapshot.color_selected})
				current_max = self.data[i]
				current_max_index = i
			else:
				self.save_snapshot(
					"'%s' nie jest większe od '%s', więc przechodzimy dalej." % (self.data[i], current_max),
					{current_max_index: Snapshot.color_current, i: Snapshot.color_selected})
		self.save_snapshot("Był to ostatni element z tablicy danych, więc algorytm kończy działanie.", {current_max_index: Snapshot.color_selected})
		self.save_snapshot("Znaleziona wartosć maksymalna wynosi '%s'." % current_max,
							{current_max_index: Snapshot.color_current_final})


def __init__():
	return MaxSearch()
