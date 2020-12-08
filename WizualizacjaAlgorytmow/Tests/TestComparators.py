from unittest import TestCase
from Comparators import Comparator, compare


class TestAlgorithm(TestCase):
	def setUp(self):
		self.comparator = Comparator()
		self.compare = compare


class TestCompare(TestAlgorithm):
	def test_is_int_greater_than_int(self):
		self.assertEqual(self.compare('100', '10', self.comparator.is_greater_than), True)

	def test_is_char_greater_than_int(self):
		self.assertEqual(self.compare('a', '10', self.comparator.is_greater_than), True)

	def test_is_char_greater_than_char(self):
		self.assertEqual(self.compare('b', 'a', self.comparator.is_greater_than), True)

	def test_is_char_greater_than_string(self):
		self.assertEqual(self.compare('b', 'aaa', self.comparator.is_greater_than), True)

	def test_is_string_greater_than_int(self):
		self.assertEqual(self.compare('aaa', '10', self.comparator.is_greater_than), True)

	def test_is_string_greater_than_char(self):
		self.assertEqual(self.compare('aaa', 'a', self.comparator.is_greater_than), True)

	def test_is_string_greater_than_string(self):
		self.assertEqual(self.compare('bbb', 'aaa', self.comparator.is_greater_than), True)

	def test_is_int_greater_or_equal_to_int(self):
		self.assertEqual(self.compare('100', '10', self.comparator.is_greater_or_equal_to), True)

	def test_is_char_greater_or_equal_to_int(self):
		self.assertEqual(self.compare('a', '10', self.comparator.is_greater_or_equal_to), True)

	def test_is_char_greater_or_equal_to_char(self):
		self.assertEqual(self.compare('b', 'a', self.comparator.is_greater_or_equal_to), True)

	def test_is_char_greater_or_equal_to_string(self):
		self.assertEqual(self.compare('b', 'aaa', self.comparator.is_greater_or_equal_to), True)

	def test_is_string_greater_or_equal_to_int(self):
		self.assertEqual(self.compare('aaa', '10', self.comparator.is_greater_or_equal_to), True)

	def test_is_string_greater_or_equal_to_char(self):
		self.assertEqual(self.compare('aaa', 'a', self.comparator.is_greater_or_equal_to), True)

	def test_is_string_greater_or_equal_to_string(self):
		self.assertEqual(self.compare('bbb', 'aaa', self.comparator.is_greater_or_equal_to), True)

	def test_is_int_greater_or_equal_to_int(self):
		self.assertEqual(self.compare('1', '1', self.comparator.is_greater_or_equal_to), True)

	def test_is_char_greater_or_equal_to_char(self):
		self.assertEqual(self.compare('a', 'a', self.comparator.is_greater_or_equal_to), True)

	def test_is_string_greater_or_equal_to_string(self):
		self.assertEqual(self.compare('aaa', 'aaa', self.comparator.is_greater_or_equal_to), True)

	def test_is_int_less_than_int(self):
		self.assertEqual(self.compare('10', '100', self.comparator.is_less_than), True)

	def test_is_int_less_than_char(self):
		self.assertEqual(self.compare('10', 'a', self.comparator.is_less_than), True)

	def test_is_int_less_than_string(self):
		self.assertEqual(self.compare('10', 'aaa', self.comparator.is_less_than), True)

	def test_is_char_less_than_char(self):
		self.assertEqual(self.compare('a', 'b', self.comparator.is_less_than), True)

	def test_is_char_less_than_string(self):
		self.assertEqual(self.compare('a', 'aaa', self.comparator.is_less_than), True)

	def test_is_string_less_than_char(self):
		self.assertEqual(self.compare('aaa', 'b', self.comparator.is_less_than), True)

	def test_is_string_less_than_string(self):
		self.assertEqual(self.compare('aaa', 'bbb', self.comparator.is_less_than), True)

	def test_is_int_less_or_equal_to_int(self):
		self.assertEqual(self.compare('10', '100', self.comparator.is_less_or_equal_to), True)

	def test_is_int_less_or_equal_to_char(self):
		self.assertEqual(self.compare('10', 'a', self.comparator.is_less_or_equal_to), True)

	def test_is_int_less_or_equal_to_string(self):
		self.assertEqual(self.compare('10', 'aaa', self.comparator.is_less_or_equal_to), True)

	def test_is_char_less_or_equal_to_char(self):
		self.assertEqual(self.compare('a', 'b', self.comparator.is_less_or_equal_to), True)

	def test_is_char_less_or_equal_to_string(self):
		self.assertEqual(self.compare('a', 'aaa', self.comparator.is_less_or_equal_to), True)

	def test_is_string_less_or_equal_to_char(self):
		self.assertEqual(self.compare('aaa', 'b', self.comparator.is_less_or_equal_to), True)

	def test_is_string_less_or_equal_to_string(self):
		self.assertEqual(self.compare('aaa', 'bbb', self.comparator.is_less_or_equal_to), True)
