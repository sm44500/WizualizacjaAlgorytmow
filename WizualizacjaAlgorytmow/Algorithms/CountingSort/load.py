import random
from Algorithms.BasicAlgorithm import BasicAlgorithm
from Snapshot import Snapshot
import numpy as np


class CountingSort(BasicAlgorithm):
	def __init__(self):
		super().__init__("CountingSort", "Sortowanie przez zliczanie")
		self.difficulty = 2
		self.counters = None
		self.local_data = None
		self.min_value = None
		self.max_value = None

	def execute(self):
		"""
		Metoda rozpoczynająca sortowanie przez zliczanie.
		"""
		self.local_data = np.array(self.data).astype("int32")
		self.min_value = self.local_data[np.argmin(self.local_data)]
		self.data_snapshot("Szukamy wartości minimalnej.")
		self.data_snapshot("Wartość minimalna wynosi '%s'." % self.min_value,
		                   {np.argmin(self.local_data): Snapshot.color_selected})
		self.max_value = self.local_data[np.argmax(self.local_data)]
		self.data_snapshot("Szukamy wartości maksymalnej.")
		self.data_snapshot("Wartość maksymalna wynosi '%s'." % self.max_value,
		                   {np.argmax(self.local_data): Snapshot.color_selected})
		self.counters = np.zeros(self.max_value-self.min_value+1)
		self.counters_snapshot("Generujemy tablicę z licznikami dla wszystkich elementów od wartości najmniejszej do wartości największej.")
		self.data_snapshot("Rozpoczynamy zliczanie - przechodzimy przez wszstkie elementy i zwiększamy odpowiednie liczniki.")
		for i in range(self.local_data.size):
			self.counters[self.local_data[i]-self.min_value] += 1
			self.data_snapshot("Zwiększamy licznik dla elementu '%s' o 1." % self.local_data[i],
			                   {i: Snapshot.color_selected})
			self.counters_snapshot("Zwiększamy licznik dla elementu '%s' o 1." % self.local_data[i],
			                       {self.local_data[i]-self.min_value: Snapshot.color_selected})
		self.data_snapshot("Po przejściu przez wszystkie elementy tablicy danych wejściowych ...")
		self.counters_snapshot("... przechodzimy przez wszystkie liczniki i wypisujemy liczby tyle razy ile wynosi wartość licznika.")
		self.data.clear()
		for i in range(len(self.counters)):
			self.counters_snapshot("Element '%i' wystąpił %i razy." % (i + self.min_value, int(self.counters[i])), {i: Snapshot.color_selected})
			for j in range(int(self.counters[i])):
				self.add_element(str(i+self.min_value))
		self.save_snapshot("Algorytm zakończył działanie!")

	def data_snapshot(self, description="", highlights={}):
		tmp = self.data.copy()
		self.data = self.local_data.astype("int32").astype("str").tolist()
		self.save_snapshot(description, highlights)
		self.data = tmp.copy()

	def counters_snapshot(self, description="", highlights={}):
		tmp = self.data.copy()
		self.data = self.counters.astype("int32").astype("str").tolist()
		for i in range(len(self.data)):
			self.data[i] = str(i+self.min_value) + ": " + str(self.data[i])
		self.save_snapshot(description, highlights)
		self.data = tmp.copy()

	def add_element(self, value: str):
		if value == '':
			pass
		elif value[0] == '-' and value[1:].isdigit():
			self.data.append(value.strip())
			self.save_snapshot("Dodanie elementu '%s' do tablicy danych." % value, {len(self.data) - 1: Snapshot.color_selected})
		elif not value.isdigit():
			self.save_snapshot("Wprowadzany element musi być liczbą.")
		else:
			self.data.append(value.strip())
			self.save_snapshot("Dodanie elementu '%s' do tablicy danych." % value, {len(self.data) - 1: Snapshot.color_selected})

	def random_data(self):
		if self.last_value == '' or not self.last_value.isdigit():
			n = 10
		else:
			n = int(self.last_value)
		for i in range(n):
			self.add_element(str(random.randint(-10, 10)))


def __init__():
	return CountingSort()
