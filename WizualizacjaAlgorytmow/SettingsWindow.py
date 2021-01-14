from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QSizePolicy

from Settings import Settings
from Styles import Styles
from Widgets.ControlPanel import ControlPanel
from Widgets.ControlPanelWidgets.ControlPanelTextBoxGroup import ControlPanelTextBoxGroup

from Paths import Paths


class SettingsWindow(QMainWindow):
	"""
	Okno odpowiedzialne za zarządzanie ustawieniami.

	Parametry:
	parent - widget rodzic.
	"""
	window_title = "Ustawienia"

	def __init__(self, parent=None):
		super().__init__(parent)
		self.control_panel = None
		self.animation_speed_slider = None
		self.shuffle_data = None
		self.input = None
		self.setup_ui()
		self.setup_buttons()

	def setup_ui(self):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.setObjectName("SettingsWindow")
		self.resize(400, 265)

		size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		size_policy.setHorizontalStretch(1)
		size_policy.setVerticalStretch(1)
		size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

		self.setSizePolicy(size_policy)
		self.setMinimumSize(QSize(400, 265))
		self.setWindowTitle(SettingsWindow.window_title)

		self.control_panel = ControlPanel(self, Qt.AlignTop)
		self.setStyleSheet(Styles.settings_background)
		self.setCentralWidget(self.control_panel)
		self.setWindowIcon(QIcon(Paths.icon("settings.png")))

	def setup_buttons(self):
		self.input = self.control_panel.add_button_group()
		self.input.set_header("Dane wejściowe")

		input_limit = self.input.add_row("Liczba elementów")
		input_limit.set_hint("Ustawienie maksymalnej liczby elementów.")
		input_limit.set_int_validator(10, 50)
		input_limit.set_value(Settings.input_limit)

		self.animation_speed_slider = self.control_panel.add_slider(1, 100, Settings.visualisation_speed, 1)
		self.animation_speed_slider.setToolTip("Ustawienie prędkości zmiany pomiędzy następnymi krokami.")

		self.shuffle_data = self.control_panel.add_button_group()
		self.shuffle_data.set_header("Losowe dane")

		minimum_value = self.shuffle_data.add_row("Minimalna wartość")
		minimum_value.set_hint("Ustawienie minimalnej wartości danego przedziału.")
		minimum_value.set_int_validator(-100, 100)
		minimum_value.set_extra_validator(Settings.random_data_maximum_value, True)
		minimum_value.set_value(Settings.random_data_minimum_value)

		maximum_value = self.shuffle_data.add_row("Maksymalna wartość")
		maximum_value.set_hint("Ustawienie maksymalnej wartości danego przedziału.")
		maximum_value.set_int_validator(-100, 100)
		maximum_value.set_extra_validator(Settings.random_data_minimum_value, False)
		maximum_value.set_value(Settings.random_data_maximum_value)

		n_elements = self.shuffle_data.add_row("Liczba danych")
		n_elements.set_hint("Liczba elementów, która zostanie wylosowana z przedziału.")
		n_elements.set_int_validator(1, 20)
		n_elements.set_value(Settings.random_data_amount)
