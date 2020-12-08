from unittest import TestCase
from Snapshot import Snapshot


class TestSnapshot(TestCase):
	def setUp(self):
		self.snapshot = Snapshot([], 'description', {})


class TestInit(TestSnapshot):
	def test_data(self):
		self.assertEqual(self.snapshot.data, [])

	def test_description(self):
		self.assertEqual(self.snapshot.description, 'description')

	def test_highlights(self):
		self.assertEqual(self.snapshot.highlights, {})


class TestColors(TestSnapshot):
	def test_color_selected(self):
		self.assertEqual(self.snapshot.color_selected, '#d0312d')

	def test_color_current(self):
		self.assertEqual(self.snapshot.color_current, '#8bc34a')

	def test_color_idle(self):
		self.assertEqual(self.snapshot.color_idle, '#87ceeb')

	def test_color_current_final(self):
		self.assertEqual(self.snapshot.color_current_final, '#ffff66')
