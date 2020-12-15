from unittest import TestCase
from AlgorithmsLogic.DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(TestCase):
	def setUp(self):
		self.doubly_linked_list = DoublyLinkedList()


class TestInit(TestDoublyLinkedList):
	def test_name(self):
		self.assertEqual(self.doubly_linked_list.name, "DoublyLinkedList")

	def test_title(self):
		self.assertEqual(self.doubly_linked_list.title, "Lista dwukierunkowa")

	def test_difficulty(self):
		self.assertEqual(self.doubly_linked_list.difficulty, 3)

