import os

class Code:
    """
    Klasa reprezentująca przykładowy kod algorytmu.

    Przykład:
    >>> code = Code()
    """
    def __init__(self):
        """
        Konstruktor klasy
        """
        self.path = ""
        self.language = ""
        self.code = ""

    @staticmethod
    def fromFile(path: str):
        """
        Wczytuje obiekt Code z pliku. Nazwa pliku do pierwszej kropki jest interpretowana jako nazwa języka.

        Parametry:
        path - Ścieżka do pliku

        Typ zwracany:
        obiekt klasy Code

        Przykład:
        >>> code = Code.fromFile("algorithm/example/c++.cpp")
        """
        code = Code()
        code.path = path
        code.language = os.path.basename(path).split(".")[0]
        file = open(path, "r")
        code.code = file.read()
        return code