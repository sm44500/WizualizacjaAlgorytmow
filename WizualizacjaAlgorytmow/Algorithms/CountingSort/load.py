from Algorithms.BasicAlgorithm import BasicAlgorithm
from Comparators import Comparator, compare
from Snapshot import Snapshot
import numpy as np


class CountingSort(BasicAlgorithm):
    def __init__(self):
        super().__init__("CountingSort", "TODO: Sortowanie przez zliczanie")
        self.difficulty = 2
        self.counters = np.array([])
        self.local_data = np.array(self.data)
        self.min_value = 0
        self.max_value = 0

    def execute(self):
        """
        Metoda rozpoczynająca sortowanie przez zliczanie.
        """

        print(self.data)
        self.local_data = np.array(self.data)
        print(self.local_data.astype("int32"))

        self.min_value = self.local_data[np.argmin(self.local_data)]
        print("a")
        self.data = self.local_data.tolist()
        self.save_snapshot("Szukamy wartości minimalnej")
        self.save_snapshot("Wartość minimalna wynosi '%s'" % self.min_value, {np.argmin(self.local_data): Snapshot.color_selected})
        print("a")
        self.max_value = self.local_data[np.argmax(self.local_data)]
        print(self.min_value, self.max_value)
        self.save_snapshot("Szukamy wartości maksymalnej")
        self.save_snapshot("Wartość maksymalna wynosi '%s'" % self.max_value, {np.argmax(self.local_data): Snapshot.color_selected})
        self.counters = np.zeros(int(self.max_value) - int(self.min_value))
        print(self.counters)
        self.data = self.counters.astype("int32").astype("str").tolist()
        print(self.data)
        self.save_snapshot("Generujemy liczniki")
        print("b")



def __init__():
    return CountingSort()
