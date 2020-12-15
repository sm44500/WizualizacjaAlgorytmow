from unittest import TestCase
from AlgorithmsLogic.Algorithm import Algorithm
from PyQt5.QtWidgets import QWidget
from Snapshot import Snapshot


class TestAlgorithm(TestCase):
	def setUp(self):
		self.algorithm = Algorithm()


class TestInit(TestAlgorithm):
	def test_visualization_widget(self):
		self.assertEqual(self.algorithm.visualization_widget, QWidget)

	def test_name(self):
		self.assertEqual(self.algorithm.name, "missing")

	def test_title(self):
		self.assertEqual(self.algorithm.title, "missing")

	def test_description(self):
		self.assertEqual(self.algorithm.description, "")

	def test_difficulty(self):
		self.assertEqual(self.algorithm.difficulty, 0)

	def test_last_value(self):
		self.assertEqual(self.algorithm.last_value, 0)

	def test_codes(self):
		self.assertEqual(self.algorithm.codes, [])

	def test_test_questions(self):
		self.assertEqual(self.algorithm.test_questions, [])

	def test_buttons(self):
		self.assertEqual(self.algorithm.buttons, None)

	def test_data(self):
		self.assertEqual(self.algorithm.data, [])

	def test_snapshots(self):
		self.assertEqual(self.algorithm.snapshots, [])


class TestSnapshot(TestAlgorithm):
	def test_save_snapshot(self):
		self.assertEqual(len(self.algorithm.snapshots), 0)
		self.algorithm.save_snapshot()
		self.assertNotEqual(len(self.algorithm.snapshots), 0)


class TestTests(TestAlgorithm):
	def test_load_test(self):
		self.assertEqual(len(self.algorithm.test_questions), 0)
		self.algorithm.load_test()
		self.assertNotEqual(len(self.algorithm.test_questions), 0)


class TestCodes(TestAlgorithm):
	def test_load_codes(self):
		self.assertEqual(len(self.algorithm.codes), 0)
		self.algorithm.load_codes()
		self.assertNotEqual(len(self.algorithm.codes), 0)
