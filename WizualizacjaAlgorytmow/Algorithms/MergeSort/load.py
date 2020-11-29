import math

from Algorithms.BasicAlgorithm import BasicAlgorithm


class MergeSort(BasicAlgorithm):
    """
    Klasa reprezentująca algorytm wyszukiwania minimum w tablicy

    Parametry:

    Przykład:

    """
    def __init__(self):
        super().__init__("MergeSort", "Sortowanie przez scalanie")

    def execute(self):
        if len(self.data) > 0:
            self.merge_sort(0, len(self.data)-1)
            self.save_snapshot("")

    def merge_sort(self, left_index, right_index):
        if left_index != right_index:
            center_index = int(math.floor((left_index + right_index)/2))

            colors = dict()
            for i in range(left_index, right_index+1):
                colors[i] = 'r' if i > center_index else 'g'

            self.save_snapshot("Dzielimy obszary", colors)
            self.merge_sort(left_index, center_index)
            self.merge_sort(center_index+1, right_index)

            self.sort(left_index, center_index, right_index)

    def sort(self, left_index, center_index, right_index):
        left_copy = self.data[left_index:center_index + 1]
        right_copy = self.data[center_index+1:right_index+1]

        # Initial values for variables that we use to keep
        # track of where we are in each array
        left_copy_index = 0
        right_copy_index = 0
        sorted_index = left_index

        colors = dict()
        for i in range(left_index, right_index+1):
            colors[i] = 'r'

        self.save_snapshot("Sortujemy..." + str(colors), colors)

        # Go through both copies until we run out of elements in one
        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

            # If our left_copy has the smaller element, put it in the sorted
            # part and then move forward in left_copy (by increasing the pointer)
            if left_copy[left_copy_index] <= right_copy[right_copy_index]:
                self.data[sorted_index] = left_copy[left_copy_index]
                left_copy_index = left_copy_index + 1
            # Opposite from above
            else:
                self.data[sorted_index] = right_copy[right_copy_index]
                right_copy_index = right_copy_index + 1

            # Regardless of where we got our element from
            # move forward in the sorted part
            sorted_index = sorted_index + 1

        # We ran out of elements either in left_copy or right_copy
        # so we will go through the remaining elements and add them
        while left_copy_index < len(left_copy):
            self.data[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1

        while right_copy_index < len(right_copy):
            self.data[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1

        self.save_snapshot("Po sortowaniu." + str(colors), colors)

        #self.save_snapshot("Sortujemy..." + str(colors), colors)

        #self.save_snapshot("Po sortowaniu." + str(colors), colors)


def __init__():
    return MergeSort()
