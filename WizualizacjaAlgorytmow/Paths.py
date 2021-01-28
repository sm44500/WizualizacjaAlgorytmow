import os
import sys


class Paths:
	"""
	Klasa pomocnicza umożliwiająca łatwy dostęp do ścierzek plików i folderów.
	Każda ścieżka jest ścieżką bezwzględną.
	"""
	if getattr(sys, 'frozen', False):
		program = os.path.dirname(sys.executable)
	else:
		program = os.path.dirname(os.path.abspath(__file__)) 
	resources = os.path.join(program, "Resources")
	icons = os.path.join(resources, "Icons")
	algorithms = os.path.join(program, "Algorithms")

	@staticmethod
	def nodz_config():
		"""
		Zwraca ścieżkę do konfiguracji biblioteki nodz.
		"""
		return os.path.join(Paths.resources, "nodz.json")

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
		return os.path.join(algorithm_path, "questions/questions.json")

	@staticmethod
	def test_question_image(algorithm_name: str, image_name:str):
		"""
		Pobiera ścieżkę do obrazka pytania.
		
		Parametry:
			algorithm_name - nazwa algorytmu

			image_name - nazwa pliku grafiki
		"""
		algorithm_path = Paths.algorithm(algorithm_name)
		question_resource = os.path.join(algorithm_path, "questions/resources")
		return os.path.join(question_resource, image_name)

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
