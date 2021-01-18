from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QColor, QFont, QIntValidator
from Styles import Styles


class ControlPanelSingleRow(QWidget):
	"""
	Klasa reprezentująca pojedynczy wiersz.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.layout = None
		self.label = None
		self.input_box = None
		self.value = None
		self.extra_value = None
		self.extra_value_should_be_greater = True
		self.minimum_value = 0
		self.maximum_value = 1
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setStyleSheet(Styles.label_background)
		self.setMinimumHeight(32)
		self.setContentsMargins(0, 0, 0, 0)

		shadow = QGraphicsDropShadowEffect()
		shadow.setOffset(1.0, 1.0)
		shadow.setColor(QColor(127, 127, 127, 255))

		font = QFont()
		font.setPointSize(11)

		self.label = QLabel(self)
		self.label.setMinimumSize(200, self.minimumHeight())
		self.label.setFont(font)
		self.label.setStyleSheet(Styles.label_background)
		self.label.setAlignment(Qt.AlignCenter)

		font = QFont()
		font.setPointSize(13)
		font.setBold(True)

		self.input_box = QLineEdit(self)
		self.input_box.setMinimumHeight(self.minimumHeight())
		self.input_box.setStyleSheet(Styles.text_box_background)
		self.input_box.setAlignment(Qt.AlignRight)
		self.input_box.setFont(font)

		self.layout = QHBoxLayout(self)
		self.layout.addWidget(self.label)
		self.layout.addWidget(self.input_box)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)

	def set_text(self, text: str):
		"""
		Ustawienie wyświetlanego tekstu.

		Parametry:
		text - tekst do wyświetlenia
		"""
		self.label.setText(" " + text + " ")

	def set_int_validator(self, minimum: int = 0, maximum: int = 100):
		"""
		Ustawienie trybu przyjmowania jedynie liczb całkowitych z podanego przedziału.

		Parametry:
		minimum - minimalna wartość jaka może wystąpić w polu tekstowym
		maximum - maksymalna wartość jaka może wystąpić w polu tekstowym
		"""
		self.minimum_value = minimum
		self.maximum_value = maximum

	def set_extra_validator(self, extra_value, extra_value_should_be_greater: bool):
		"""
		Dodanie dodatkowych walidacji danych.
		"""
		self.extra_value = extra_value
		self.extra_value_should_be_greater = extra_value_should_be_greater

	def set_value(self, value):
		"""
		Ustawienie wartości i podpięcie funkcji aktualizującej tą wartość po zmianie jej w panelu.

		Parametry:
		value - tablica jednoelementowa z wartością przeznaczoną do zmiany
		"""
		self.input_box.setText(str(value[0]))
		self.input_box.textChanged.connect(self.update_value)
		self.value = value

	def update_value(self):
		"""
		Aktualizacja zmiennej po każdej zmianie.
		"""
		if self.input_box.text() == "-":
			return

		try:
			local_value = int(self.input_box.text())
		except ValueError:
			local_value = 0

		if self.extra_value:
			if self.extra_value_should_be_greater:
				local_value = min(local_value, self.extra_value[0])
			else:
				local_value = max(local_value, self.extra_value[0])

		local_value = min(max(local_value, self.minimum_value), self.maximum_value)
		self.value[0] = local_value
		self.input_box.setText(str(local_value))

	def set_hint(self, hint: str):
		"""
		Ustawienie podpowiedzi na danym polu.

		Parametry:
		hint - tekst wyświetlany jako podpowiedź
		"""
		self.label.setToolTip(hint)
		self.input_box.setToolTip(hint)


class ControlPanelTextBoxGroup(QWidget):
	"""
	Panel kontrolny z grupą podpisanych klawiszy.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent)
		self.header = None
		self.layout = None
		self.rows = list()
		self.setup_ui()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setStyleSheet(Styles.label_background)
		self.setMinimumHeight(32)
		self.setContentsMargins(0, 0, 0, 0)

		shadow = QGraphicsDropShadowEffect()
		shadow.setOffset(1.0, 1.0)
		shadow.setColor(QColor(127, 127, 127, 255))

		font = QFont()
		font.setPointSize(14)
		font.setBold(True)

		self.header = QLabel()
		self.header.setFont(font)
		self.header.setStyleSheet(Styles.label_background)
		self.header.setGraphicsEffect(shadow)
		self.header.setAlignment(Qt.AlignCenter)
		self.header.setMinimumHeight(self.minimumHeight())

		self.layout = QVBoxLayout(self)
		self.layout.addWidget(self.header)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setSpacing(0)

	def set_header(self, text: str):
		"""
		Ustawienie nagłówka panelu.

		Parametry:
		text - treść nagłówka
		"""
		self.header.setText(text)

	def add_row(self, text: str) -> ControlPanelSingleRow:
		"""
		Dodanie nowego wiersza.

		Parametry:
		text - wartość tekstowa pola

		Typ zwracany:
		ControlPanelSingleRow - klasa reprezentująca pojedyńczy wiersz
		"""
		row = ControlPanelSingleRow(self)
		row.set_text(text)

		self.rows.append(row)
		self.layout.addWidget(row)

		return row
