from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from Widgets.ControlPanelWidgets.ControlPanelSlider import ControlPanelSlider
from Widgets.ControlPanelWidgets.ControlPanelButton import ControlPanelButton
from Widgets.ControlPanelWidgets.ControlPanelLabel import ControlPanelLabel
from Widgets.ControlPanelWidgets.ControlPanelTextBox import ControlPanelTextBox
from Widgets.ControlPanelWidgets.ControlPanelIconPanel import ControlPanelIconPanel
from Widgets.ControlPanelWidgets.ControlPanelTextBoxGroup import ControlPanelTextBoxGroup
from Widgets.BaseWidget import BaseWidget


class ControlPanel(BaseWidget):
	"""
	Klasa reprezentująca panel kontrolny.

	Parametry:
		parent - widget rodzic.
		alignment - wyrównanie, domyślnie Qt.AlignTop
	"""

	def __init__(self, parent=None, alignment=Qt.AlignTop):
		super().__init__(parent, QVBoxLayout)
		self.widgets = []
		self.setup_ui(alignment)

	def setup_ui(self, alignment):
		"""
		Inicjalizacja interfejsu użytkownika.
		"""
		self.widget_layout.setContentsMargins(10, 10, 10, 10)
		self.widget_layout.setAlignment(alignment)

	def clear(self):
		"""
		Czyści panel z widget'ów
		"""
		for widget in self.widgets:
			widget.setParent(None)
		self.widgets = []

	def add_icon_panel(self) -> ControlPanelIconPanel:
		"""
		Dodaje panel z ikonami do panelu.

		Powrót:
			ControlPanelIconPanel - Panel z ikonami
		"""
		icon_panel = ControlPanelIconPanel()
		self.widget_layout.addWidget(icon_panel)
		self.widgets.append(icon_panel)
		return icon_panel

	def add_button(self, text, icon_path="", hint="") -> ControlPanelButton:
		"""
		Dodaje przycisk do panelu.

		Parametry:
			text - tekst wyświetlany na przycisku
			icon_path - ścieżka do ikony (opcjonalnie)
			hint - tekst po najechaniu kursowem (opcjonalnie)

		Powrót:
			ControlPanelButton - przycisk
		"""
		button = ControlPanelButton()
		button.set_icon(icon_path)
		button.set_hint(hint)
		button.set_text(text)
		self.widget_layout.addWidget(button)
		self.widgets.append(button)
		return button

	def add_label(self, text) -> ControlPanelLabel:
		"""
		Dodaje etykietę do panelu.

		Parametry:
			text - tekst wyświetlany na etykiecie

		Powrót:
			ControlPanelLabel - przycisk
		"""
		label = ControlPanelLabel()
		label.setText(text)
		self.widget_layout.addWidget(label)
		self.widgets.append(label)
		return label

	def add_text_box(self, hint: str) -> ControlPanelTextBox:
		"""
		Dodaje pole tekstowe do panelu.

		Powrót:
			ControlPanelTextBox - przycisk
		"""
		text_box = ControlPanelTextBox()
		text_box.setToolTip(hint)
		self.widget_layout.addWidget(text_box)
		self.widgets.append(text_box)
		return text_box

	def add_slider(self, minimum, maximum, value, step) -> ControlPanelSlider:
		"""
		Dodaje suwak do panelu.

		Parametry:
			minimum - wartość minimalna suwaka
			maximum - wartość maksymalna suwaka
			value - wartość domyślna suwaka
			step - krok zmiany wartości suwaka

		Powrót:
			ControlPanelSlider - suwak
		"""
		slider = ControlPanelSlider(value, Qt.Horizontal)
		slider.setMinimum(minimum)
		slider.setMaximum(maximum)
		slider.setSingleStep(step)
		self.add_label("Prędkość animacji:").setMinimumHeight(32)
		self.widget_layout.addWidget(slider)
		self.widgets.append(slider)
		return slider

	def add_button_group(self) -> ControlPanelTextBoxGroup:
		"""
		Dodanie grupy klawiszy.

		Typ zwracany:
		ControlPanelButtonGroup
		"""
		buttons = ControlPanelTextBoxGroup()

		self.widget_layout.addWidget(buttons)
		self.widgets.append(buttons)

		return buttons
