from unittest import TestCase
from Algorithms.BinarySearch.load import BinarySearch


class TestBinarySearchTestCase(TestCase):
	def setUp(self):
		self.binary_search = BinarySearch()


class TestInit(TestBinarySearchTestCase):
	def test_name(self):
		self.assertEqual(self.binary_search.name, "BinarySearch")

	def test_title(self):
		self.assertEqual(self.binary_search.title, "Wyszukiwanie binarne")

	def test_difficulty(self):
		self.assertEqual(self.binary_search.difficulty, 2)


class TestExecute(TestBinarySearchTestCase):
	def test_found_index(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('2')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(index, 1)

	def test_found_value(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('2')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(value, '2')

	def test_not_found_index(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(index, "not_found")

	def test_not_found_value(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(value, "not_found")