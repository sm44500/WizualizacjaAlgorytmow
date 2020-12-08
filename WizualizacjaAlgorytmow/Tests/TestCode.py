from unittest import TestCase

from PyQt5.QtCore import QUrl

from Code import Code
from Paths import Paths


class TestCode(TestCase):
	def setUp(self):
		self.code = Code()
		self.code_cpp = self.code.from_file("Algorithms/BinarySearch/codes/c++.html")
		self.code_pseudocode = self.code.from_file("Algorithms/BinarySearch/codes/pseudocode.html")
		self.code_python = self.code.from_file("Algorithms/BinarySearch/codes/python.html")


class TestInit(TestCode):
	def test_path(self):
		self.assertEqual(self.code_cpp.path, "Algorithms/BinarySearch/codes/c++.html")
		self.assertEqual(self.code_pseudocode.path, "Algorithms/BinarySearch/codes/pseudocode.html")
		self.assertEqual(self.code_python.path, "Algorithms/BinarySearch/codes/python.html")

	def test_language(self):
		self.assertEqual(self.code_cpp.language, "c++")
		self.assertEqual(self.code_pseudocode.language, "pseudocode")
		self.assertEqual(self.code_python.language, "python")

	def test_url(self):
		self.assertEqual(self.code_cpp.url, QUrl.fromLocalFile(self.code_cpp.path))
		self.assertEqual(self.code_pseudocode.url, QUrl.fromLocalFile(self.code_pseudocode.path))
		self.assertEqual(self.code_python.url, QUrl.fromLocalFile(self.code_python.path))

	def test_icon(self):
		self.assertEqual(self.code_cpp.icon, Paths.icon("c++.png"))
		self.assertEqual(self.code_pseudocode.icon, Paths.icon("code.png"))
		self.assertEqual(self.code_python.icon, Paths.icon("python.png"))



