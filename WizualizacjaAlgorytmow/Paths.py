import os


class Paths:
	"""
	Klasa pomocnicza umożliwiająca łatwy dostęp do ścierzek plików i folderów.
	Każda ścieżka jest ścieżką bezwzględną.
	"""
	program = os.path.dirname(os.path.abspath(__file__))
	resources = os.path.join(program, "Resources")
	icons = os.path.join(resources, "Icons")
	algorithms = os.path.join(program, "Algorithms")

	@staticmethod
	def icon(icon_file: str):
		"""
		Pobiera ikonę.

		Parametry:
		icon_file - nazwa pliku ikony
		"""
		return os.path.join(Paths.icons, icon_file)

	@staticmethod
	def algorithm(algorithm_name: str):
		"""
		Pobiera ścieżkę do algorytmu.
		
		Parametry:
		algorithm_name - nazwa algorytmu
		"""
		return os.path.join(Paths.algorithms, algorithm_name)

	@staticmethod
	def codes(algorithm_name: str):
		"""
		Pobiera ścieżkę do folderu z kodami danego algorytmu.
		
		Parametry:
		algorithm_name - nazwa algorytmu
		"""
		algorithm_path = Paths.algorithm(algorithm_name)
		return os.path.join(algorithm_path, "codes")

	@staticmethod
	def test(algorithm_name: str):
		"""
		Pobiera ścieżkę do pliku testu z pytaniami danego algorytmu.
		
		Parametry:
		algorithm_name - nazwa algorytmu
		"""
		algorithm_path = Paths.algorithm(algorithm_name)
		return os.path.join(algorithm_path, "test.json")

	@staticmethod
	def description(algorithm_name: str):
		"""
		Pobiera ścieżkę do pliku z opisem danego algorytmu.
		
		Parametry:
		algorithm_name - nazwa algorytmu
		"""
		algorithm_path = Paths.algorithm(algorithm_name)
		return os.path.join(algorithm_path, "description/description.html")

	@staticmethod
	def logic(algorithm_name: str):
		"""
		Pobiera ścieżkę do pliku z logiką algorytmu.
		
		Parametry:
		algorithm_name - nazwa algorytmu
		"""
		algorithm_path = Paths.algorithm(algorithm_name)
		return os.path.join(algorithm_path, "load.py")
