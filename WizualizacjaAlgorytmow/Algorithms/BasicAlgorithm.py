from Algorithms.Algorithm import Algorithm
from Visualisation.BasicAlgorithmVisualisation import BasicAlgorithmVisualisation


class BasicAlgorithm(Algorithm):
	"""
	Klasa abstrakcyjna reprezentująca algorytm z kategori łatwe (difficulty=1)
    (algorytm wykorzystujący bibliotekę NetworkX)

	Parametry:
	name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.
    title - pełna nazwa algorytmu. Wyswietlana w aplikacji.

	Przykład:
	>>> min_search = BasicAlgorithm("MinSearch")
	"""
	def __init__(self, name: str = "missing", title: str = "missing"):
		super().__init__(name, title)
		self.value = 3
		self.visualization_widget = BasicAlgorithmVisualisation
		self.buttons = list()
		self.buttons.append(["Dodaj element", lambda: self.add_element(self.value)])
		self.buttons.append(["Usun element", lambda: self.remove_element(self.value)])
		self.buttons.append(["Wykonaj", lambda: self.execute()])
		self.save_snapshot("")

	def add_element(self, value):
        """
       	Metoda dodawająca element o podanej wartosci do tablicy wejsciowej.
       
       	Parametry:
       	value - wartosć elementu, który ma zostać dodany
       
       	Przykład:
       	>>> add_element(5)
	    """
        if self.data.count(value) == 0:
            self.data.append(int(value))
            self.save_snapshot("Dodanie wartosci %s" % value, {len(self.data)-1: 'r'})

	def remove_element(self, value):
        """
    	Metoda usuwająca pierwszy element o podanej wartosci z tablicy wejsciowej.
    
    	Parametry:
    	value - wartosć elementu, który ma zostać usunięty
    
    	Przykład:
    	>>> remove_element(5)
    	"""
		if self.data.count(value) > 0:
			self.data.remove(value)
			self.save_snapshot("Usuniecie wartosci %i" % value)

	def execute(self):
        """
    	Abstrakcyjna metoda uruchamiająca algorytm.
    	"""
		pass
