from collections import defaultdict


class Snapshot:
	"""
	Klasa reprezentująca pojedyńczy krok wykonywania algorytmu.

	Parametry:
	data - stan algorytmu
	description - opis kroku
	highlights - elementy wyróżnione

	Przykład:
	>>> Snapshot([1, 2, 3], "Dodanie elementu '3' na koniec tablicy danych.", {2: '#ff0000'})
	"""
	color_selected = '#d0312d'
	color_current = '#8bc34a'
	color_idle = '#87ceeb'
	color_current_final = '#ffff66'
	color_group1 = color_selected
	color_group2 = color_current

	def __init__(self, data, description: str, highlights: dict):
		self.data = data
		self.description = description
		self.highlights = defaultdict(lambda: Snapshot.color_idle, highlights)
