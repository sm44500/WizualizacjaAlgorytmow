import importlib.util
import os

from Algorithms.Algorithm import Algorithm
from Paths import Paths


def get_algorithm_list() -> list:
	"""
	Funkcja wczytujacą wszystkie algorytmy.

	Typ zwracany:
	list - lista przechowująca wszystkie obiekty, które dziedziczą po Algorithm.

	Przykład:
	>>> algorithms = get_algorithm_list()
	"""
	algorithms = []
	for module in os.listdir(Paths.algorithms):
		algorithm_directory = Paths.algorithm(module)

		if module == "__pycache__":
			continue

		if not os.path.isdir(algorithm_directory):
			continue

		algorithm_init_file = Paths.logic(module)
		if not os.path.isfile(algorithm_init_file):
			print("Missing load.py file! (%s)" % (module))
			continue

		spec = importlib.util.spec_from_file_location("module.name", algorithm_init_file)
		foo = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(foo)
		algorithm = foo.__init__()
		if not isinstance(algorithm, Algorithm):
			print("Object is not instance of Algorithm! (%s)" % module)
			continue

		if algorithm.name == "missing":
			continue

		algorithm.name = module
		algorithm.load_test()
		algorithm.load_codes()
		algorithms.append(algorithm)

	algorithms.sort(key=lambda algo: algo.difficulty)
	return algorithms
