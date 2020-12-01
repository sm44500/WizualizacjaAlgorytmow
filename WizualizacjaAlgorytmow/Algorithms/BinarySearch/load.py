from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot


class BinarySearch(BasicAlgorithm):
	"""
	Klasa reprezentująca algorytm wyszukiwania binarnego.

	Przykład:
	>>> binary_search = BinarySearch()
	"""

	def __init__(self):
		super().__init__("BinarySearch", "Wyszukiwanie binarne")
		self.difficulty = 2

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		self.data.sort()
		self.save_snapshot("Na początek sortujemy tablicę wejściową.")
		left_index = 0
		right_index = len(self.data)-1

		while left_index <= right_index:
			center_index = int((right_index-left_index)/2)
			self.save_snapshot("Wyznaczamy element środkowy.", {center_index: Snapshot.color_selected})


def __init__():
	return BinarySearch()
