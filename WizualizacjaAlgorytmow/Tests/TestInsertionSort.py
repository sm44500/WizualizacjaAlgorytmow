from unittest import TestCase
from AlgorithmsLogic.InsertionSort import InsertionSort


class TestInsertionSort(TestCase):
	def setUp(self):
		self.insertion_sort = InsertionSort()


class TestInit(TestInsertionSort):
	def test_name(self):
		self.assertEqual(self.insertion_sort.name, "InsertionSort")

	def test_title(self):
		self.assertEqual(self.insertion_sort.title, "Sortowanie przez wstawianie")

	def test_difficulty(self):
		self.assertEqual(self.insertion_sort.difficulty, 2)


class TestExecute(TestInsertionSort):
	def test_int_sort(self):
		self.insertion_sort.add_element('3')
		self.insertion_sort.add_element('2')
		self.insertion_sort.add_element('1')
		self.insertion_sort.execute()
		self.assertEqual(self.insertion_sort.data[0], '1')
		self.assertEqual(self.insertion_sort.data[1], '2')
		self.assertEqual(self.insertion_sort.data[2], '3')

	def test_char_sort(self):
		self.insertion_sort.add_element('c')
		self.insertion_sort.add_element('b')
		self.insertion_sort.add_element('a')
		self.insertion_sort.execute()
		self.assertEqual(self.insertion_sort.data[0], 'a')
		self.assertEqual(self.insertion_sort.data[1], 'b')
		self.assertEqual(self.insertion_sort.data[2], 'c')

	def test_string_sort(self):
		self.insertion_sort.add_element('ccc')
		self.insertion_sort.add_element('bbb')
		self.insertion_sort.add_element('aaa')
		self.insertion_sort.execute()
		self.assertEqual(self.insertion_sort.data[0], 'aaa')
		self.assertEqual(self.insertion_sort.data[1], 'bbb')
		self.assertEqual(self.insertion_sort.data[2], 'ccc')