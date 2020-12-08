from unittest import TestCase
from Algorithms.MinSearch.load import MinSearch


class TestMinSearch(TestCase):
	def setUp(self):
		self.min_search = MinSearch()


class TestInit(TestMinSearch):
	def test_name(self):
		self.assertEqual(self.min_search.name, "MinSearch")

	def test_title(self):
		self.assertEqual(self.min_search.title, "Wyszukiwanie wartości minimalnej")

	def test_difficulty(self):
		self.assertEqual(self.min_search.difficulty, 1)


class TestExecute(TestMinSearch):
	def test_found_index(self):
		self.min_search.add_element('1')
		self.min_search.add_element('2')
		self.min_search.add_element('3')
		index, value = self.min_search.execute()
		self.assertEqual(index, 0)

	def test_found_value(self):
		self.min_search.add_element('1')
		self.min_search.add_element('2')
		self.min_search.add_element('3')
		index, value = self.min_search.execute()
		self.assertEqual(value, '1')
