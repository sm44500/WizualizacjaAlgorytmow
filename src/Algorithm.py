from PyQt5.QtWidgets import QWidget
import os
import json

from TestQuestion import TestQuestion
from Code import Code

class Algorithm:
    """
    Klasa abstrakcyjna reprezentująca algorytm

    Przykład:
    >>> algorithm = Algorithm("bst")
    """
    def __init__(self, name: str):
        """
        Konstruktor klasy

        Parametry:
        name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.
        """
        self.widget = QWidget()
        self.name = name
        self.description = ""
        self.path = open(os.path.join("./algorithm", self.name))
        self.codes = []
        self.test_questions = []
        __loadTest()
        __loadCodes()


    def __loadTest(self):
        file = os.path.join(self.path, "test.json")
        self.test_questions = TestQuestion.fromFile(file)

        
    def __loadCodes(self):
        codes_path = os.path.join(self.path, "codes")
        codes_files = os.listdir(codes_path)
        for code_file in codes_files:
            code_file_path = os.path.join(codes_path, code_file)
            code = Code.fromFile(code_file_path)
            self.codes.append(code)