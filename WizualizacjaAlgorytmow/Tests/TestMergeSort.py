from unittest import TestCase
from AlgorithmsLogic.MergeSort import MergeSort


class TestMergeSort(TestCase):
	def setUp(self):
		self.merge_sort = MergeSort()


class TestInit(TestMergeSort):
	def test_name(self):
		self.assertEqual(self.merge_sort.name, "MergeSort")

	def test_title(self):
		self.assertEqual(self.merge_sort.title, "Sortowanie przez scalanie")

	def test_difficulty(self):
		self.assertEqual(self.merge_sort.difficulty, 3)


class TestExecute(TestMergeSort):
	def test_int_sort(self):
		self.merge_sort.add_element('3')
		self.merge_sort.add_element('2')
		self.merge_sort.add_element('1')
		self.merge_sort.execute()
		self.assertEqual(self.merge_sort.data[0], '1')
		self.assertEqual(self.merge_sort.data[1], '2')
		self.assertEqual(self.merge_sort.data[2], '3')

	def test_char_sort(self):
		self.merge_sort.add_element('c')
		self.merge_sort.add_element('b')
		self.merge_sort.add_element('a')
		self.merge_sort.execute()
		self.assertEqual(self.merge_sort.data[0], 'a')
		self.assertEqual(self.merge_sort.data[1], 'b')
		self.assertEqual(self.merge_sort.data[2], 'c')

	def test_string_sort(self):
		self.merge_sort.add_element('ccc')
		self.merge_sort.add_element('bbb')
		self.merge_sort.add_element('aaa')
		self.merge_sort.execute()
		self.assertEqual(self.merge_sort.data[0], 'aaa')
		self.assertEqual(self.merge_sort.data[1], 'bbb')
		self.assertEqual(self.merge_sort.data[2], 'ccc')