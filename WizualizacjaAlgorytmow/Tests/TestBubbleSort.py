from unittest import TestCase
from Algorithms.BubbleSort.load import BubbleSort


class TestBubbleSort(TestCase):
	def setUp(self):
		self.bubble_sort = BubbleSort()


class TestInit(TestBubbleSort):
	def test_name(self):
		self.assertEqual(self.bubble_sort.name, "BubbleSort")

	def test_title(self):
		self.assertEqual(self.bubble_sort.title, "Sortowanie bąbelkowe")

	def test_difficulty(self):
		self.assertEqual(self.bubble_sort.difficulty, 1)


class TestExecute(TestBubbleSort):
	def test_int_sort(self):
		self.bubble_sort.add_element('3')
		self.bubble_sort.add_element('2')
		self.bubble_sort.add_element('1')
		self.bubble_sort.execute()
		self.assertEqual(self.bubble_sort.data[0], '1')
		self.assertEqual(self.bubble_sort.data[1], '2')
		self.assertEqual(self.bubble_sort.data[2], '3')

	def test_char_sort(self):
		self.bubble_sort.add_element('c')
		self.bubble_sort.add_element('b')
		self.bubble_sort.add_element('a')
		self.bubble_sort.execute()
		self.assertEqual(self.bubble_sort.data[0], 'a')
		self.assertEqual(self.bubble_sort.data[1], 'b')
		self.assertEqual(self.bubble_sort.data[2], 'c')

	def test_string_sort(self):
		self.bubble_sort.add_element('ccc')
		self.bubble_sort.add_element('bbb')
		self.bubble_sort.add_element('aaa')
		self.bubble_sort.execute()
		self.assertEqual(self.bubble_sort.data[0], 'aaa')
		self.assertEqual(self.bubble_sort.data[1], 'bbb')
		self.assertEqual(self.bubble_sort.data[2], 'ccc')