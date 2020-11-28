from collections import defaultdict


class Snapshot:
	def __init__(self, data, description: str, highlights: dict):
		self.data = data
		self.description = description
		self.highlights = defaultdict(lambda: 'b', highlights)
