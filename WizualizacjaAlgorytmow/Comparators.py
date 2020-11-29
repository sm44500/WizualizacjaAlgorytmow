def compare(a: str, b: str, comparator) -> bool:
	"""
	Metoda porównująca dwa elementy.
	Istotne jest to, że implementacja musi wyglądać w ten sposób, bo przechowując w tablicy same teksty
	porównania dla liczb mogłby nie funkcjonować poprawnie. To znaczy na przykład '2' byłoby większe od '41'.

	Parametry:
	a - pierwsza wartość.
	b - druga wartość.
	comparator - funkcja porównująca.

	Zwracany typ:
	bool - wynik porównania dwóch wartości.
	"""
	if (a.isdigit() and b.isdigit() and comparator(float(a), float(b))) or comparator(a, b):
		return True

	return False


class Comparator:
	@staticmethod
	def is_greater_than(a: str, b: str):
		return a > b

	@staticmethod
	def is_greater_or_equal_to(a: str, b: str):
		return a >= b

	@staticmethod
	def is_less_than(a: str, b: str):
		return a < b

	@staticmethod
	def is_less_or_equal_to(a: str, b: str):
		return a <= b
