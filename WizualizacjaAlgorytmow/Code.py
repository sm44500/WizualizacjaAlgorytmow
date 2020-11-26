import os
from PyQt5.QtCore import QUrl
from Paths import Paths
class Code:
    """
    Klasa reprezentująca przykładowy kod algorytmu.

    Przykład:
    >>> code = Code()
    """
    def __init__(self):
        self.path = ""
        self.language = ""
        self.url = ""
        self.icon = ""

    @staticmethod
    def from_file(path: str):
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
        code.url = QUrl.fromLocalFile(code.path)
        code.language = os.path.basename(path).split(".")[0]
        icon_file = code.language + ".png"
        code.icon = Paths.icon(icon_file)
        if not os.path.isfile(code.icon):
            code.icon = Paths.icon("code.png")
        return code