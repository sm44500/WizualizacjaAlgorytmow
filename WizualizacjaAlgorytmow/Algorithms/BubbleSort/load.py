from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot


class BubbleSort(BasicAlgorithm):
	def __init__(self):
		super().__init__("BubbleSort", "Sortowanie bąbelkowe")
		self.difficulty = 1

	def execute(self):
		self.save_snapshot("Rozpoczynamy sortowanie bąbelkowe...")
		size = len(self.data)
		for i in range(size):
			j = 0
			last_index = size - (i + 1)
			if last_index >= 1:
				colors = dict()
				for c in range(last_index + 1):
					colors[c] = Snapshot.color_selected
				self.save_snapshot("Sortujemy elementy od indeksu %i. do indeksu %i." % (0, last_index), colors)

			while j < last_index:
				self.save_snapshot("Sprawdzamy czy '%s' jest większe niż '%s'." % (self.data[j], self.data[j + 1]),
									{j: Snapshot.color_selected, j + 1: Snapshot.color_selected})

				if compare(self.data[j], self.data[j + 1], Comparator.is_greater_than):
					self.save_snapshot(
						"'%s' jest większe niż '%s', tak więc zamieniamy je miejscami." % (self.data[j], self.data[j + 1]),
						{j: Snapshot.color_selected, j + 1: Snapshot.color_selected})
					temporary = self.data[j]
					self.data[j] = self.data[j + 1]
					self.data[j + 1] = temporary
					self.save_snapshot("Po zamianie miejscami.",
									{j: Snapshot.color_current, j + 1: Snapshot.color_current})
				else:
					self.save_snapshot(
						"'%s' nie jest większe niż '%s', tak więc sprawdzamy dalej." % (self.data[j], self.data[j + 1]),
						{j: Snapshot.color_selected, j + 1: Snapshot.color_selected})
				j += 1
			if i == 0:
				self.save_snapshot("Na koniec trafił największy element ze zbioru.",
									{len(self.data) - 1: Snapshot.color_current})
			elif i < len(self.data) - 2:
				self.save_snapshot("Rozpoczynamy kolejną iterację.")
		self.save_snapshot("Algorytm zakończył działanie!")


def __init__():
	return BubbleSort()
