from Algorithms.BasicAlgorithm import BasicAlgorithm
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
		value = self.last_value
		left_index = 0
		right_index = len(self.data) - 1
		found_index = -1

		while left_index <= right_index:
			center_index = (right_index + left_index) // 2
			self.save_snapshot("Wyznaczamy element środkowy.", {center_index: Snapshot.color_selected})

			if value == self.data[center_index]:
				found_index = center_index
				break
			elif value < self.data[center_index]:
				right_index = center_index - 1
				colors = dict()
				for i in range(left_index, right_index + 1):
					colors[i] = Snapshot.color_selected
				self.save_snapshot("lewa połówka.", colors)
			else:
				left_index = center_index + 1
				colors = dict()
				for i in range(left_index, right_index + 1):
					colors[i] = Snapshot.color_selected
				self.save_snapshot("prawa połówka.", colors)

		if found_index >= 0:
			self.save_snapshot("Znaleziono wyszukiwaną wartość w elemencie środkowym.")
		else:
			self.save_snapshot("nie Znaleziono wyszukiwaną wartość w elemencie środkowym.")


def __init__():
	return BinarySearch()
