import random

from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot
import numpy as np


class CountingSort(BasicAlgorithm):
	def __init__(self):
		super().__init__("CountingSort", "TODO: Sortowanie przez zliczanie")
		self.difficulty = 2
		self.counters = None
		self.local_data = None

	def execute(self):
		"""
		Metoda rozpoczynająca sortowanie przez zliczanie.
		"""
		self.counters = np.zeros(21)
		self.local_data = np.array(self.data)

	def data_snapshot(self, description="", highlights={}):
		self.data = self.local_data.astype("int32").astype("str").tolist()
		self.save_snapshot(description, highlights)

	def counters_snapshot(self, description="", highlights={}):
		self.data = self.counters.astype("int32").astype("str").tolist()
		self.save_snapshot(description, highlights)

	def add_element(self, value: str):
		if value == '' or not value.isdigit() or int(value) < 0 or int(value) > 20:
			self.save_snapshot("W celu czytelnej wizualizacji należy wprowadzić liczbę z przedziału <0;20>")
		else:
			self.data.append(value.strip())
			self.save_snapshot("Dodanie elementu '%s' do tablicy danych." % value,
			                   {len(self.data) - 1: Snapshot.color_selected})

	def random_data(self):
		if self.last_value == '' or not self.last_value.isdigit():
			n = 10
		else:
			n = int(self.last_value)
		for i in range(n):
			self.add_element(str(random.randint(0, 20)))


def __init__():
	return CountingSort()
