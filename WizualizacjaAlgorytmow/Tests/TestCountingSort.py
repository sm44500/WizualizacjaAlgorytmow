from unittest import TestCase
from AlgorithmsLogic.CountingSort import CountingSort


class TestCountingSort(TestCase):
	def setUp(self):
		self.counting_sort = CountingSort()


class TestInit(TestCountingSort):
	def test_name(self):
		self.assertEqual(self.counting_sort.name, "CountingSort")

	def test_title(self):
		self.assertEqual(self.counting_sort.title, "Sortowanie przez zliczanie")

	def test_difficulty(self):
		self.assertEqual(self.counting_sort.difficulty, 3)


class TestExecute(TestCountingSort):
	def test_int_sort(self):
		self.counting_sort.add_element('3')
		self.counting_sort.add_element('2')
		self.counting_sort.add_element('1')
		self.counting_sort.execute()
		self.assertEqual(self.counting_sort.data[0], '1')
		self.assertEqual(self.counting_sort.data[1], '2')
		self.assertEqual(self.counting_sort.data[2], '3')
