from unittest import TestCase
from Algorithms.Node import Node


class TestNode(TestCase):
	def setUp(self):
		self.node = Node('value', 'next_node', 'previous_node')


class TestInit(TestNode):
	def test_value(self):
		self.assertEqual(self.node.value, 'value')

	def test_next_node(self):
		self.assertEqual(self.node.next_node, 'next_node')

	def test_previous_node(self):
		self.assertEqual(self.node.previous_node, 'previous_node')
