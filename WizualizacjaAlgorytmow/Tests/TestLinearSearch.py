from unittest import TestCase
from Algorithms.LinearSearch.load import LinearSearch


class TestLinearSearch(TestCase):
	def setUp(self):
		self.linear_search = LinearSearch()


class TestInit(TestLinearSearch):
	def test_name(self):
		self.assertEqual(self.linear_search.name, "LinearSearch")

	def test_title(self):
		self.assertEqual(self.linear_search.title, "Wyszukiwanie liniowe")

	def test_difficulty(self):
		self.assertEqual(self.linear_search.difficulty, 1)


class TestExecute(TestLinearSearch):
	def test_int_found_index(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('2')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(index, 1)

	def test_int_found_value(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('2')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(value, '2')

	def test_int_not_found_index(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(index, "not_found")

	def test_int_not_found_value(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(value, "not_found")

	def test_char_found_index(self):
		self.linear_search.add_element('a')
		self.linear_search.add_element('b')
		self.linear_search.add_element('c')
		self.linear_search.last_value = 'b'
		index, value = self.linear_search.execute()
		self.assertEqual(index, 1)

	def test_char_found_value(self):
		self.linear_search.add_element('a')
		self.linear_search.add_element('b')
		self.linear_search.add_element('c')
		self.linear_search.last_value = 'b'
		index, value = self.linear_search.execute()
		self.assertEqual(value, 'b')

	def test_char_not_found_index(self):
		self.linear_search.add_element('a')
		self.linear_search.add_element('c')
		self.linear_search.last_value = 'b'
		index, value = self.linear_search.execute()
		self.assertEqual(index, "not_found")

	def test_char_not_found_value(self):
		self.linear_search.add_element('a')
		self.linear_search.add_element('c')
		self.linear_search.last_value = 'b'
		index, value = self.linear_search.execute()
		self.assertEqual(value, "not_found")

	def test_string_found_index(self):
		self.linear_search.add_element('aaa')
		self.linear_search.add_element('bbb')
		self.linear_search.add_element('ccc')
		self.linear_search.last_value = 'bbb'
		index, value = self.linear_search.execute()
		self.assertEqual(index, 1)

	def test_string_found_value(self):
		self.linear_search.add_element('aaa')
		self.linear_search.add_element('bbb')
		self.linear_search.add_element('ccc')
		self.linear_search.last_value = 'bbb'
		index, value = self.linear_search.execute()
		self.assertEqual(value, 'bbb')

	def test_string_not_found_index(self):
		self.linear_search.add_element('aaa')
		self.linear_search.add_element('ccc')
		self.linear_search.last_value = 'bbb'
		index, value = self.linear_search.execute()
		self.assertEqual(index, "not_found")

	def test_string_not_found_value(self):
		self.linear_search.add_element('aaa')
		self.linear_search.add_element('ccc')
		self.linear_search.last_value = 'bbb'
		index, value = self.linear_search.execute()
		self.assertEqual(value, "not_found")