from PyQt5.QtWidgets import QWidget
from copy import deepcopy

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
	def __init__(self, name: str = "missing", title: str = "missing"):
		self.visualization_widget = QWidget
		self.name = name
		self.title = title
		self.difficulty = 0
		self.textbox_value = 0
		self.codes = []
		self.test_questions = []
		self.controls = []
		self.data = []
		self.snapshots = []
		self.__load_codes()
		self.__load_test()

	def save_snapshot(self, description: str = "", highlights: dict = {}):
		"""
		Metoda zapisująca aktualny stan tablicy z danymi.

		Parametry:
		description - opis zmian dokonanych w zapisywanym stanie.
		highlights - słownik z węzłami oznaczonymi innym kolorem.
		"""
		self.snapshots.append(Snapshot(deepcopy(self.data), description, highlights))

	def add_button(self, title: str, callback, icon="", hint="" , update=True):
		"""
		Dodaje przycisk.

		Parametry:
			title - tekst na przycisku
			callback - funkcja wywoływana przy przyciśnięciu przycisku.
			icon - ścieżka do ikony przycisku. Domyślnie brak.
			hint - tekst wyświetlany po najechaniu na przycisk. Domyślnie pusty.
			update - wartość True, False. Określa czy po wykonaniu interakcji, wizualizacja ma pokazać ostatni krok. Domyślne True.
		"""
		self.controls.append(["BUTTON", title, callback, icon, hint, update])

	def add_textbox(self, label: str, callback, hint="" , update=False):
		"""
		Dodaje pole tekstowe.

		Parametry:
			label - Etykieta pola tekstowego.
			callback - funkcja wywoływana przy zmianie wartości pola. Jej pierwszy parametr będzie zawierał wartość.
			hint - tekst wyświetlany po najechaniu na pole tekstowe. Domyślnie pusty.
			update - wartość True, False. Określa czy po wykonaniu interakcji, wizualizacja ma pokazać ostatni krok. Domyślne False.
		"""
		self.controls.append(["TEXTBOX", label, callback, hint, update])

	def __load_test(self):
		"""
		Metoda importująca pytania testowe do algorytmu.
		"""
		self.test_questions = []
		test_path = Paths.test(self.name)
		self.test_questions = TestQuestion.from_file(test_path)
		
	def __load_codes(self):
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
