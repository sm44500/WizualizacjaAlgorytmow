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
		self.codes = None
		self.test_questions = None
		self.buttons = None
		self.data = []
		self.snapshots = []
		self.current_snapshot_index = 0

	def next_snapshot(self):
		"""
		Przechodzi oraz zwraca następny krok.

		Typ zwracany:
		obiekt klasy Snapshot
		"""
		self.current_snapshot_index = max(0, min(self.current_snapshot_index+1, len(self.snapshots)-1))
		return self.snapshots[self.current_snapshot_index]

	def previous_snapshot(self):
		"""
		Przechodzi oraz zwraca poprzedni krok.

		Typ zwracany:
		obiekt klasy Snapshot
		"""
		self.current_snapshot_index = max(0, min(self.current_snapshot_index-1, len(self.snapshots)-1))
		return self.snapshots[self.current_snapshot_index]
		
	def first_snapshot(self):
		"""
		Zwraca pierwszy krok.

		Typ zwracany:
		obiekt klasy Snapshot
		"""
		self.current_snapshot_index = 0
		return self.snapshots[self.current_snapshot_index]

	def last_snapshot(self):
		"""
		Zwraca ostatni krok.

		Typ zwracany:
		obiekt klasy Snapshot
		"""
		self.current_snapshot_index = max(0, len(self.snapshots) - 1)
		return self.snapshots[self.current_snapshot_index]

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
		self.test_questions = list()
		test_path = Paths.test(self.name)
		self.test_questions = TestQuestion.from_file(test_path)
		
	def load_codes(self):
		"""
		Metoda importująca przykładowe kody do algorytmu.
		"""
		self.codes = list()
		codes_path = Paths.codes(self.name)
		codes_files = os.listdir(codes_path)
		for code_file in codes_files:
			code_file_path = os.path.join(codes_path, code_file)
			code = Code.from_file(code_file_path)
			self.codes.append(code)
