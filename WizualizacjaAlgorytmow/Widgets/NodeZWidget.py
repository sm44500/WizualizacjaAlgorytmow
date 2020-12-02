from PyQt5.QtWidgets import QGridLayout, QLabel
from Widgets.BaseWidget import BaseWidget


class NodeZWidget(BaseWidget):
	"""
	Widget wizualizacji opartej na bibliotece NodeZ.

	Parametry:
	parent - widget rodzic.
	"""
	def __init__(self, parent=None):
		super().__init__(parent, QGridLayout)