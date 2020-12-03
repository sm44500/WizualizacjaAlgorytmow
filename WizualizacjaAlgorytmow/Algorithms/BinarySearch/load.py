from Algorithms.BasicAlgorithm import BasicAlgorithm
from Snapshot import Snapshot
from Comparators import Comparator, compare


class BinarySearch(BasicAlgorithm):
	"""
	Klasa reprezentująca algorytm wyszukiwania binarnego.

	Przykład:
	>>> binary_search = BinarySearch()
	"""

	def __init__(self):
		super().__init__("BinarySearch", "Wyszukiwanie binarne")
		self.difficulty = 2

	def bubble_sort(self):
		"""
		Metoda wykonująca sortowanie bąbelkowe na danych wejściowych.
		"""
		n = len(self.data)
		for i in range(n - 1):
			for j in range(0, n - i - 1):
				if compare(self.data[j], self.data[j + 1], Comparator.is_greater_than):
					self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		self.bubble_sort()
		self.save_snapshot("Na początek sortujemy tablicę wejściową.")
		value = self.last_value
		left_index = 0
		right_index = len(self.data)
		found_index = -1

		colors = dict()
		while left_index <= right_index:
			center_index = (right_index + left_index) // 2
			colors[center_index] = Snapshot.color_selected
			self.save_snapshot("Wyznaczamy element środkowy.", colors)
			self.save_snapshot("Sprawdzamy czy szukana wartość '%s' jest równa wartości elementu środkowego '%s'." %(value, self.data[center_index]), colors)

			#self.save_snapshot("Wyznaczamy element środkowy.", {center_index: Snapshot.color_selected})
			#self.save_snapshot("Sprawdzamy czy szukana wartość '%s' jest równa wartości elementu środkowego '%s'." %(value, self.data[center_index]), {center_index: Snapshot.color_selected})
			if value == self.data[center_index]:
				found_index = center_index
				break
			elif value < self.data[center_index]:
				right_index = center_index - 1
				colors = dict()
				for i in range(left_index, right_index + 1):
					colors[i] = Snapshot.color_current
				self.save_snapshot("Szukana wartość '%s' jest mniejsza od wartości elementu środkowego '%s', więc przeszukujemy elementy na lewo od elementu środkowego." %(value, self.data[center_index]), colors)
			else:
				left_index = center_index + 1
				colors = dict()
				for i in range(left_index, right_index + 1):
					colors[i] = Snapshot.color_current
				self.save_snapshot("Szukana wartość '%s' jest większa od wartości elementu środkowego '%s', więc przeszukujemy elementy na prawo od elementu środkowego." %(value, self.data[center_index]), colors)

		if found_index >= 0:
			self.save_snapshot("Szukana wartość '%s' została znaleziona na pozycji %s." % (value, found_index), {found_index: Snapshot.color_current_final})
		else:
			self.save_snapshot("Szukana wartość '%s' nie została znaleziona." % value)


def __init__():
	return BinarySearch()
