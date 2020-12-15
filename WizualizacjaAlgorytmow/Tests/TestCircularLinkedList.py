from unittest import TestCase
from AlgorithmsLogic.CircularLinkedList import CircularLinkedList


class TestCircularLinkedList(TestCase):
	def setUp(self):
		self.circular_linked_list = CircularLinkedList()


class TestInit(TestCircularLinkedList):
	def test_name(self):
		self.assertEqual(self.circular_linked_list.name, "CircularLinkedList")

	def test_title(self):
		self.assertEqual(self.circular_linked_list.title, "Lista cykliczna")

	def test_difficulty(self):
		self.assertEqual(self.circular_linked_list.difficulty, 3)

