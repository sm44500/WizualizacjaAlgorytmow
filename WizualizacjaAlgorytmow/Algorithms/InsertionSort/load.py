from Algorithms.BasicAlgorithm import BasicAlgorithm
from Snapshot import Snapshot
from Comparators import Comparator, compare


class InsertionSort(BasicAlgorithm):
    def __init__(self):
        super().__init__("InsertionSort", "TODO: Sortowanie przez wstawianie")
        self.difficulty = 2

    def execute(self):
        for i in range(1, len(self.data)):
            value = self.data[i]
            j = i - 1
            while j >= 0 and compare(self.data[j], value, Comparator.is_greater_than):
                self.data[j + 1] = self.data[j]
                j = j - 1
                self.save_snapshot("x", {j: Snapshot.color_selected})
            self.data[j + 1] = value


def __init__():
    return InsertionSort()
