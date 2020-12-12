from AlgorithmsLogic.BasicAlgorithm import BasicAlgorithm
from Snapshot import Snapshot
from Comparators import Comparator, compare


class InsertionSort(BasicAlgorithm):
	def __init__(self):
		super().__init__("InsertionSort", "Sortowanie przez wstawianie")
		self.difficulty = 2

	def execute(self):
		for i in range(1, len(self.data)):
			value = self.data[i]
			j = i - 1
			self.save_snapshot(
				"Zapamiętujemy wartość %s. elementu ('%s') i szukamy dla niego odpowiedniego miejsca po lewej stronie, tak, aby po jego lewej stronie stał element o mniejszej wartości, a po prawej stronie element o większej wartości." % (i, value),
				{i: Snapshot.color_current})
			while j >= 0 and compare(self.data[j], value, Comparator.is_greater_than):
				self.save_snapshot(
					"Element '%s' jest mniejszy od '%s', więc sprawdzamy wartość kolejnego elementu po lewej." % (
						value, self.data[j]), {j: Snapshot.color_selected})
				self.data[j + 1] = self.data[j]
				j = j - 1
			self.data[j + 1] = value
			if j == -1:
				self.save_snapshot(
					"Nie ma więcej elementów po lewej stronie, więc element '%s' został umieszczony na pozycji %s." % (
						value, j + 1), {j + 1: Snapshot.color_current_final})
			else:
				self.save_snapshot("Element '%s' nie jest mniejszy od '%s', więc został umieszczony na pozycji %s." % (
					value, self.data[j], j + 1), {j + 1: Snapshot.color_current_final})
		self.save_snapshot("Algorytm zakończył działanie!")
