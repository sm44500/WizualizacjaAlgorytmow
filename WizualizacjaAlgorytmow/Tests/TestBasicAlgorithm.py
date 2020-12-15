from unittest import TestCase
from AlgorithmsLogic.BasicAlgorithm import BasicAlgorithm
from Widgets.NetworkXWidget import NetworkXWidget
from Snapshot import Snapshot


class TestBasicAlgorithm(TestCase):
	def setUp(self):
		self.basic_algorithm = BasicAlgorithm()


class TestInit(TestBasicAlgorithm):
	def test_visualization_widget(self):
		self.assertEqual(self.basic_algorithm.visualization_widget, NetworkXWidget)

	def test_load_buttons(self):
		self.assertNotEqual(len(self.basic_algorithm.buttons), 0)

	def test_data_clear(self):
		self.assertEqual(len(self.basic_algorithm.data), 0)

	def test_snapshots_clear(self):
		self.assertEqual(len(self.basic_algorithm.snapshots), 0)


class TestAddElement(TestBasicAlgorithm):
	def test_add_int(self):
		self.basic_algorithm.add_element('1')
		self.assertEqual(self.basic_algorithm.data[0], '1')

	def test_add_char(self):
		self.basic_algorithm.add_element('a')
		self.assertEqual(self.basic_algorithm.data[0], 'a')

	def test_add_string(self):
		self.basic_algorithm.add_element('aaa')
		self.assertEqual(self.basic_algorithm.data[0], 'aaa')


class TestRemoveElement(TestBasicAlgorithm):
	def test_remove_int(self):
		self.basic_algorithm.add_element('1')
		self.assertEqual(self.basic_algorithm.remove_element('1'), True)

	def test_remove_char(self):
		self.basic_algorithm.add_element('a')
		self.assertEqual(self.basic_algorithm.remove_element('a'), True)

	def test_remove_string(self):
		self.basic_algorithm.add_element('aaa')
		self.assertEqual(self.basic_algorithm.remove_element('aaa'), True)

	def test_not_remove_int(self):
		self.assertEqual(self.basic_algorithm.remove_element('1'), False)

	def test_not_remove_char(self):
		self.assertEqual(self.basic_algorithm.remove_element('a'), False)

	def test_not_remove_string(self):
		self.assertEqual(self.basic_algorithm.remove_element('aaa'), False)


class TestRemoveAllElements(TestBasicAlgorithm):
	def test_remove_all_int(self):
		self.basic_algorithm.add_element('1')
		self.basic_algorithm.add_element('1')
		self.basic_algorithm.add_element('1')
		self.basic_algorithm.remove_all_elements('1')
		self.assertEqual(len(self.basic_algorithm.data), 0)

	def test_remove_all_char(self):
		self.basic_algorithm.add_element('a')
		self.basic_algorithm.add_element('a')
		self.basic_algorithm.add_element('a')
		self.basic_algorithm.remove_all_elements('a')
		self.assertEqual(len(self.basic_algorithm.data), 0)

	def test_remove_all_string(self):
		self.basic_algorithm.add_element('aaa')
		self.basic_algorithm.add_element('aaa')
		self.basic_algorithm.add_element('aaa')
		self.basic_algorithm.remove_all_elements('aaa')
		self.assertEqual(len(self.basic_algorithm.data), 0)

	def test_not_remove_all_int(self):
		self.basic_algorithm.remove_all_elements('1')
		self.assertEqual(len(self.basic_algorithm.data), 0)

	def test_not_remove_all_char(self):
		self.basic_algorithm.remove_all_elements('a')
		self.assertEqual(len(self.basic_algorithm.data), 0)

	def test_not_remove_all_string(self):
		self.basic_algorithm.remove_all_elements('aaa')
		self.assertEqual(len(self.basic_algorithm.data), 0)


class TestClear(TestBasicAlgorithm):
	def test_clear_data(self):
		self.basic_algorithm.add_element('1')
		self.basic_algorithm.clear()
		self.assertEqual(len(self.basic_algorithm.data), 0)
		self.assertEqual(len(self.basic_algorithm.snapshots), 1)

	def test_clear_no_data(self):
		self.basic_algorithm.clear()
		self.assertEqual(len(self.basic_algorithm.data), 0)
		self.assertEqual(len(self.basic_algorithm.snapshots), 1)


class TestShuffle(TestBasicAlgorithm):
	def test_shuffle_data(self):
		self.basic_algorithm.last_value = '100'
		self.basic_algorithm.random_data()
		before = self.basic_algorithm.data.copy()
		self.basic_algorithm.shuffle()
		after = self.basic_algorithm.data.copy()
		self.assertNotEqual(before, after)

	def test_shuffle_no_data(self):
		self.basic_algorithm.shuffle()


class TestRandomData(TestBasicAlgorithm):
	def test_random_data_not_set_value(self):
		self.basic_algorithm.last_value = ''
		self.basic_algorithm.random_data()
		self.assertEqual(len(self.basic_algorithm.data), 10)

	def test_random_data_set_value(self):
		self.basic_algorithm.last_value = '100'
		self.basic_algorithm.random_data()
		self.assertEqual(len(self.basic_algorithm.data), 100)


class TestLoadButtons(TestBasicAlgorithm):
	def test_load_buttons(self):
		self.basic_algorithm.load_buttons()
		self.assertEqual(len(self.basic_algorithm.buttons), 7)
