from unittest import TestCase
from Algorithms.MaxSearch.load import MaxSearch


class TestMaxSearch(TestCase):
	def setUp(self):
		self.max_search = MaxSearch()


class TestInit(TestMaxSearch):
	def test_name(self):
		self.assertEqual(self.max_search.name, "MaxSearch")

	def test_title(self):
		self.assertEqual(self.max_search.title, "Wyszukiwanie wartości maksymalnej")

	def test_difficulty(self):
		self.assertEqual(self.max_search.difficulty, 1)


class TestExecute(TestMaxSearch):
	def test_found_index(self):
		self.max_search.add_element('1')
		self.max_search.add_element('2')
		self.max_search.add_element('3')
		index, value = self.max_search.execute()
		self.assertEqual(index, 2)

	def test_found_value(self):
		self.max_search.add_element('1')
		self.max_search.add_element('2')
		self.max_search.add_element('3')
		index, value = self.max_search.execute()
		self.assertEqual(value, '3')
