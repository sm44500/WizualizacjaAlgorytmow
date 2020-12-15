from unittest import TestCase
from AlgorithmsLogic.AdvancedAlgorithm import AdvancedAlgorithm
from Widgets.NodZWidget import NodZWidget
from Snapshot import Snapshot


class TestAdvancedAlgorithm(TestCase):
	def setUp(self):
		self.advanced_algorithm = AdvancedAlgorithm()


class TestInit(TestAdvancedAlgorithm):
	def test_visualization_widget(self):
		self.assertEqual(self.advanced_algorithm.visualization_widget, NodZWidget)

	def test_load_buttons(self):
		self.assertNotEqual(len(self.advanced_algorithm.buttons), 0)

	def test_data_clear(self):
		self.assertEqual(len(self.advanced_algorithm.data), 0)

	def test_snapshots_clear(self):
		self.assertEqual(len(self.advanced_algorithm.snapshots), 0)


class TestClear(TestAdvancedAlgorithm):
	def test_clear_data(self):
		#self.advanced_algorithm.add_element('1')
		self.advanced_algorithm.clear()
		self.assertEqual(len(self.advanced_algorithm.data), 0)
		self.assertEqual(len(self.advanced_algorithm.snapshots), 1)

	def test_clear_no_data(self):
		self.advanced_algorithm.clear()
		self.assertEqual(len(self.advanced_algorithm.data), 0)
		self.assertEqual(len(self.advanced_algorithm.snapshots), 1)


class TestLoadButtons(TestAdvancedAlgorithm):
	def test_load_buttons(self):
		self.advanced_algorithm.load_buttons()
		self.assertEqual(len(self.advanced_algorithm.buttons), 0)
