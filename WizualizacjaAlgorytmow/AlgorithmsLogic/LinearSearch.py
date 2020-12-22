from AlgorithmsLogic.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot


class LinearSearch(BasicAlgorithm):
	"""
	Klasa reprezentująca algorytm wyszukiwania elementu w tablicy

	Przykład:
		>>> linear_search = LinearSearch()
	"""

	def __init__(self):
		super().__init__("LinearSearch", "Wyszukiwanie liniowe")
		self.difficulty = 1
		self.found = False

	def execute(self):
		"""
		Metoda uruchamiająca algorytm.
		"""
		for i in range(len(self.data)):
			self.save_snapshot(
				"Porównujemy %s. element z tablicy o wartości '%s' z wyszukiwanym elementem '%s'." % (i, self.data[i], self.textbox_value),
				{i: Snapshot.color_current})
			if self.data[i] == self.textbox_value:
				found_index = i
				found_value = self.data[i]
				self.save_snapshot("Znaleziono element o wartości '%s'" % (self.data[i]), {i: Snapshot.color_current_final})
				self.found = True
				break
			else:
				self.save_snapshot("'%s' nie jest równe '%s', więc przechodzimy dalej." % (self.data[i], self.textbox_value),{i: Snapshot.color_current})
		if not self.found:
			found_index = "not_found"
			found_value = "not_found"
			self.save_snapshot("Wyszukiwany element nie został znaleziony.")
		return found_index, found_value
