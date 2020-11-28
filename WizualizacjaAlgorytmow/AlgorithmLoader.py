import importlib.util
import os

from Algorithms.Algorithm import Algorithm


def get_algorithm_list(directory: str = "Algorithms", filename: str = "load.py") -> list:
	"""
	Funkcja wczytujacą wszystkie algorytmy.

	Parametry:
	directory - folder z wszystkimi algorytmami
	filename - nazwa pliku który zostanie wczytany z folderu

	Przykład:
	>>> algorithms = get_algorithm_list()
	"""
	current_path = os.path.dirname(__file__)
	algorithms_path = current_path + "\\" + directory + "\\"
	algorithms = list()
	for module in os.listdir(algorithms_path):
		algorithm_directory = algorithms_path + module

		if module == "__pycache__":
			continue

		if not os.path.isdir(algorithm_directory):
			continue

		algorithm_init_file = algorithm_directory + "\\" + filename
		if not os.path.isfile(algorithm_init_file):
			print("Missing %s file! (%s)" % (filename, module))
			continue

		spec = importlib.util.spec_from_file_location("module.name", algorithm_init_file)
		foo = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(foo)
		algorithm = foo.__init__()
		if not isinstance(algorithm, Algorithm):
			print("Object is not instance of Algorithm! (%s)" % module)
			continue

		algorithm.name = module
		algorithm.load_test()
		algorithm.load_codes()
		algorithms.append(algorithm)

	return algorithms
