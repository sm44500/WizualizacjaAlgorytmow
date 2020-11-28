from Algorithms.Algorithm import Algorithm


class BasicAlgorithm(Algorithm):
	"""
	Klasa abstrakcyjna reprezentująca łatwy algorytm (algorytm wykorzystujący bibliotekę NetworkX)

	Parametry:
	name - skrótowa nazwa algorytmu. Tożsama z nazwą w folderze algorithm.

	Przykład:
	>>> bs = BasicAlgorithm("bubble_sort")
	"""

	def __init__(self, name: str = "missing", title: str = "missing"):
		super().__init__(name, title)
		self.value = 3
		self.buttons = list()
		self.buttons.append(["Dodaj element", lambda: self.add_element(self.value)])
		self.buttons.append(["Usun element", lambda: self.remove_element(self.value)])
		self.buttons.append(["Debug print", lambda: print(self.data)])

	def add_element(self, value):
		self.data.append(value)
		self.save_snapshot("Dodanie wartosci " + str(value))
		print(value)

	def remove_element(self, value):
		if self.data.count(value) > 0:
			self.data.remove(value)
			self.save_snapshot("Usuniecie wartosci " + str(value))

	def execute(self):
		pass
