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
	def test_found_index(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('2')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(index, 1)

	def test_found_value(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('2')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(value, '2')

	def test_not_found_index(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(index, "not_found")

	def test_not_found_value(self):
		self.linear_search.add_element('1')
		self.linear_search.add_element('3')
		self.linear_search.last_value = '2'
		index, value = self.linear_search.execute()
		self.assertEqual(value, "not_found")