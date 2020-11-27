from PyQt5.QtWidgets import QWidget
import os
import json

from Paths import Paths
from TestQuestion import TestQuestion
from Code import Code

class Algorithm:
    """
    Klasa abstrakcyjna reprezentująca algorytm

    Parametry:
    name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.

    Przykład:
    >>> algorithm = Algorithm("bst")
    """
    def __init__(self, name: str, title: str):
        self.visualization_widget = QWidget
        self.name = name
        self.title = title
        self.description = ""
        self.codes = []
        self.test_questions = []
        self.__load_test()
        self.__load_codes()
        self.buttons = []

    def __load_test(self):
        test_path = Paths.test(self.name)
        self.test_questions = TestQuestion.from_file(test_path)
        
    def __load_codes(self):
        codes_path = Paths.codes(self.name)
        codes_files = os.listdir(codes_path)
        for code_file in codes_files:
            code_file_path = os.path.join(codes_path, code_file)
            code = Code.from_file(code_file_path)
            self.codes.append(code)
