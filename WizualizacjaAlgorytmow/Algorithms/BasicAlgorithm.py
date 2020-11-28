from Algorithms.Algorithm import Algorithm

class BasicAlgorithm(Algorithm):
    """
    Klasa abstrakcyjna reprezentująca łatwy algorytm (algorytm wykorzystujący bibliotekę NetworkX)

    Parametry:
    name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.

    Przykład:
    >>> bs = BasicAlgorithm("bubble_sort")
    """
    def __init__(self, name: str, title: str):
        super().__init__(name, title)
        
    def add_element(self,value):
        self.data.append(value)
        self.save_snapshot("Dodanie wartosci " + str(value))
        
    def delete_element(self,value):
        self.data.remove(value)
        self.save_snapshot("Usuniecie wartosci " + str(value))
        
    def execute(self):
        pass