from unittest import TestCase
from AlgorithmsLogic.ListAlgorithm import ListAlgorithm
from Widgets.NodZWidget import NodZWidget
from Snapshot import Snapshot


class TestListAlgorithm(TestCase):
	def setUp(self):
		self.list_algorithm = ListAlgorithm()

class TestInit(TestListAlgorithm):
	def test_visualization_widget(self):
		self.assertEqual(self.list_algorithm.visualization_widget, NodZWidget)

	def test_load_buttons(self):
		self.assertNotEqual(len(self.list_algorithm.buttons), 0)

	def test_data_clear(self):
		self.assertEqual(len(self.list_algorithm.data), 0)

	def test_snapshots_clear(self):
		self.assertEqual(len(self.list_algorithm.snapshots), 0)


class TestClear(TestListAlgorithm):
	def test_clear_data(self):
		#self.list_algorithm.add_element('1')
		self.list_algorithm.clear()
		self.assertEqual(len(self.list_algorithm.data), 0)
		self.assertEqual(len(self.list_algorithm.snapshots), 1)

	def test_clear_no_data(self):
		self.list_algorithm.clear()
		self.assertEqual(len(self.list_algorithm.data), 0)
		self.assertEqual(len(self.list_algorithm.snapshots), 1)


class TestLoadButtons(TestListAlgorithm):
	def test_load_buttons(self):
		self.list_algorithm.load_buttons()
		self.assertEqual(len(self.list_algorithm.buttons), 0)
