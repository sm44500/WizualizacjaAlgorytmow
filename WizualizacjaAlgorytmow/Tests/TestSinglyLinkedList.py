from unittest import TestCase
from AlgorithmsLogic.SinglyLinkedList import SinglyLinkedList


class TestSinglyLinkedList(TestCase):
	def setUp(self):
		self.singly_linked_list = SinglyLinkedList()


class TestInit(TestSinglyLinkedList):
	def test_name(self):
		self.assertEqual(self.singly_linked_list.name, "SinglyLinkedList")

	def test_title(self):
		self.assertEqual(self.singly_linked_list.title, "Lista jednokierunkowa")

	def test_difficulty(self):
		self.assertEqual(self.singly_linked_list.difficulty, 2)

