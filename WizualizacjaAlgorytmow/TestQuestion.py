import os
import json

class TestQuestion:
	"""
	Klasa reprezentująca pytanie testowe.

	Przykład:
		>>> testQuestion = TestQuestion()
	"""
	def __init__(self):
		self.question = ""
		self.answers = []
		self.correct = -1

	def check(self, answer: int):
		"""
		Sprawdza czy podany numer odpowiedzi jest poprawną odpowiedzią

		Parametry:
			answer - int, numer odpowiedzi 

		Powrót:
			bool

		Przykład:
			>>> testQuestion.check(0)
			true
		"""
		if self.correct == answer:
			return True
		False

	def get_correct(self):
		"""
		Zwraca poprawną odpowiedz jako tekst

		Powrót:
			str

		Przykład:
			>>> testQuestion.getCorrect()
			"Przykładowa poprawna odpowiedz"
		"""
		return self.answers[self.correct]

	@staticmethod
	def from_file(path: str):
		"""
		Wczytuje obiekty TestQuestion z pliku json.

		Parametry:
			path - Ścieżka do pliku

		Powrót:
			List - Lista obiektów TestQuestion

		Przykład:
			>>> questions = Code.fromFile("algorithm/example/test.cpp")
		"""
		questions = []
		file = open(path, "r")
		json_file = json.load(file)
		for json_object in json_file:
			question = TestQuestion()
			question.question = json_object["question"]
			question.answers = json_object["answers"]
			question.correct = json_object["correct"]
			question.reason = "test uzasadnienie test" # json_object["explain"]
			questions.append(question)

		file.close()

		return questions
	