from unittest import TestCase
from Algorithms.BinarySearch.load import BinarySearch


class TestBinarySearch(TestCase):
	def setUp(self):
		self.binary_search = BinarySearch()


class TestInit(TestBinarySearch):
	def test_name(self):
		self.assertEqual(self.binary_search.name, "BinarySearch")

	def test_title(self):
		self.assertEqual(self.binary_search.title, "Wyszukiwanie binarne")

	def test_difficulty(self):
		self.assertEqual(self.binary_search.difficulty, 2)


class TestExecute(TestBinarySearch):
	def test_int_found_index(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('2')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(index, 1)

	def test_int_found_value(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('2')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(value, '2')

	def test_int_not_found_index(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(index, "not_found")

	def test_int_not_found_value(self):
		self.binary_search.add_element('1')
		self.binary_search.add_element('3')
		self.binary_search.last_value = '2'
		index, value = self.binary_search.execute()
		self.assertEqual(value, "not_found")

	def test_char_found_index(self):
		self.binary_search.add_element('a')
		self.binary_search.add_element('b')
		self.binary_search.add_element('c')
		self.binary_search.last_value = 'b'
		index, value = self.binary_search.execute()
		self.assertEqual(index, 1)

	def test_char_found_value(self):
		self.binary_search.add_element('a')
		self.binary_search.add_element('b')
		self.binary_search.add_element('c')
		self.binary_search.last_value = 'b'
		index, value = self.binary_search.execute()
		self.assertEqual(value, 'b')

	def test_char_not_found_index(self):
		self.binary_search.add_element('a')
		self.binary_search.add_element('c')
		self.binary_search.last_value = 'b'
		index, value = self.binary_search.execute()
		self.assertEqual(index, "not_found")

	def test_char_not_found_value(self):
		self.binary_search.add_element('a')
		self.binary_search.add_element('c')
		self.binary_search.last_value = 'b'
		index, value = self.binary_search.execute()
		self.assertEqual(value, "not_found")

	def test_string_found_index(self):
		self.binary_search.add_element('aaa')
		self.binary_search.add_element('bbb')
		self.binary_search.add_element('ccc')
		self.binary_search.last_value = 'bbb'
		index, value = self.binary_search.execute()
		self.assertEqual(index, 1)

	def test_string_found_value(self):
		self.binary_search.add_element('aaa')
		self.binary_search.add_element('bbb')
		self.binary_search.add_element('ccc')
		self.binary_search.last_value = 'bbb'
		index, value = self.binary_search.execute()
		self.assertEqual(value, 'bbb')

	def test_string_not_found_index(self):
		self.binary_search.add_element('aaa')
		self.binary_search.add_element('ccc')
		self.binary_search.last_value = 'bbb'
		index, value = self.binary_search.execute()
		self.assertEqual(index, "not_found")

	def test_string_not_found_value(self):
		self.binary_search.add_element('aaa')
		self.binary_search.add_element('ccc')
		self.binary_search.last_value = 'bbb'
		index, value = self.binary_search.execute()
		self.assertEqual(value, "not_found")