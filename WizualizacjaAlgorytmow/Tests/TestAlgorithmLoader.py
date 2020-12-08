from unittest import TestCase
from AlgorithmLoader import get_algorithm_list


class TestAlgorithmLoader(TestCase):
	def setUp(self):
		self.get_algorithm_list = get_algorithm_list


class TestGetAlgorithmList(TestAlgorithmLoader):
	def test_get_algorithm_list(self):
		self.assertNotEqual(len(self.get_algorithm_list()), 0)
