from PyQt5.QtWidgets import QWidget
import os
import json

from Paths import Paths
from TestQuestion import TestQuestion
from Code import Code
from Snapshot import Snapshot


class Algorithm:
	"""
	Klasa abstrakcyjna reprezentująca algorytm.

	Parametry:
	name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.
	title - pełna nazwa algorytmu. Wyswietlana w aplikacji.
	"""
	def __init__(self, name: str, title: str):
		self.visualization_widget = QWidget
		self.name = name
		self.title = title
		self.description = ""
		self.difficulty = 0
		self.last_value = 0
		self.codes = []
		self.test_questions = []
		self.buttons = None
		self.data = []
		self.snapshots = []

	def save_snapshot(self, description: str, highlights: dict = {}):
		"""
		Metoda zapisująca aktualny stan tablicy z danymi.

		Parametry:
		description - opis zmian dokonanych w zapisywanym stanie.
		highlights - słownik z węzłami oznaczonymi innym kolorem.
		"""
		self.snapshots.append(Snapshot(self.data.copy(), description, highlights))

	def load_test(self):
		"""
		Metoda importująca pytania testowe do algorytmu.
		"""
		self.test_questions = []
		test_path = Paths.test(self.name)
		self.test_questions = TestQuestion.from_file(test_path)
		
	def load_codes(self):
		"""
		Metoda importująca przykładowe kody do algorytmu.
		"""
		self.codes = []
		codes_path = Paths.codes(self.name)
		codes_files = os.listdir(codes_path)
		for code_file in codes_files:
			code_file_path = os.path.join(codes_path, code_file)
			if os.path.isfile(code_file_path) and code_file.split(".")[-1].lower() == "html":
				code = Code.from_file(code_file_path)
				self.codes.append(code)
