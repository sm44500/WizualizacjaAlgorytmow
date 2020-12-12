import math

from AlgorithmsLogic.BasicAlgorithm import BasicAlgorithm
from Snapshot import Snapshot
from Comparators import Comparator, compare


class MergeSort(BasicAlgorithm):
    """
    Klasa reprezentująca algorytm sortowania przez scalanie.
    """
    def __init__(self):
        super().__init__("MergeSort", "Sortowanie przez scalanie")
        self.difficulty = 3

    def execute(self):
        """
        Metoda uruchamiająca algorytm sortowania przez scalanie.
        """
        if len(self.data) > 0:
            self.merge_sort(0, len(self.data)-1)
            self.save_snapshot("Algorytm zakończył działanie!")

    def merge_sort(self, left_index, right_index, is_right_side: bool = False):
        """
        Metoda odpowiedzialna za rekurencyjną część algorytmu.
        """
        if left_index != right_index:
            center_index = int(math.floor((left_index + right_index)/2))

            colors = dict()
            for i in range(left_index, right_index+1):
                colors[i] = Snapshot.color_group1 if i <= center_index else Snapshot.color_group2

            self.save_snapshot("Dzielimy obszary na połowę i zajmujemy się lewą stroną.", colors)
            self.merge_sort(left_index, center_index)
            self.save_snapshot("Po skończeniu operacji na lewej stronie zajmujemy się teraz prawą stroną.", colors)
            self.merge_sort(center_index+1, right_index, True)
            self.save_snapshot("Łączymy lewą i prawą stronę.", colors)
            self.sort(left_index, center_index, right_index, is_right_side)
        else:
            colors = {left_index: Snapshot.color_group1 if not is_right_side else Snapshot.color_group2}
            self.save_snapshot("Przestajemy dzielić bo w grupie znajduje się już tylko jeden element.", colors)

    def sort(self, left_index, center_index, right_index, is_right_side: bool = False):
        """
        Metoda odpowiedzialna za sortowanie zbioru.

        Parametry:
        left_index - indeks lewego krańca.
        center_index - indeks środka.
        right_index - indeks prawego krańca.
        is_right_side - zmienna logiczna reprezentująca czy jesteśmy po lewej czy po prawej stronie zbioru.
        """
        colors = dict()
        for i in range(left_index, right_index + 1):
            colors[i] = Snapshot.color_group1 if not is_right_side else Snapshot.color_group2

        if right_index - left_index > 1:
            self.save_snapshot("Sortujemy elementy od indeksu %s. do indeksu %s." % (left_index, right_index), colors)
        else:
            self.save_snapshot("Sortujemy elementy o indeksie %s. oraz indeksie %s." % (left_index, right_index), colors)

        left_copy = self.data[left_index:center_index+1]
        right_copy = self.data[center_index+1:right_index+1]

        left_copy_index = 0
        right_copy_index = 0
        sorted_index = left_index

        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
            if compare(left_copy[left_copy_index], right_copy[right_copy_index], Comparator.is_less_than):
                self.data[sorted_index] = left_copy[left_copy_index]
                left_copy_index = left_copy_index + 1
            else:
                self.data[sorted_index] = right_copy[right_copy_index]
                right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1

        while left_copy_index < len(left_copy):
            self.data[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1

        while right_copy_index < len(right_copy):
            self.data[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1

        self.save_snapshot("Stan po sortowaniu.", colors)
