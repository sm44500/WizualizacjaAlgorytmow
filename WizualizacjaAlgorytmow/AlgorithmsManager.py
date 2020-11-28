from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Algorithms.Algorithm import Algorithm
from Paths import Paths

from AlgorithmLoader import *

class AlgorithmsManager:
    def __init__(self, main_widget: QWidget):
        self.algorithms = get_algorithm_list()
        self.main_widget = main_widget
        self.combobox = self.main_widget.top_widget
        self.control_panel = self.main_widget.middle_widget.right_widget
        self.center = self.main_widget.middle_widget.left_widget
        self.bottom = self.main_widget.bottom_widget
        self.current_index = 0
        self.current_algorithm = None
        self.setup_algorithms()

    def setup_algorithms(self):
        # Ui
        self.combobox.clear()
        for algorithm in self.algorithms:
            self.combobox.add_algorithms(algorithm.title)

        # Events
        self.main_widget.top_widget.currentIndexChanged.connect(self.on_change_algorithm)

        # Setup
        self.set_algorithm(0)

    def setup_control_panel(self):
        self.control_panel.clear()
        self.description_button = self.control_panel.add_button("Opis", Paths.icon("bookmark.png"))
        self.description_button.clicked.connect(self.show_description)
        self.questions_button = self.control_panel.add_button("Pytania", Paths.icon("question_mark.png"))

        self.codes_buttons = []
        for index, code in enumerate(self.current_algorithm.codes):
            code_button = self.control_panel.add_button("Kod " + code.language, code.icon)
            code_button.clicked.connect(lambda: self.on_click_code(index))
            self.codes_buttons.append(code_button)

        self.text_box = self.control_panel.add_text_box()
        self.codes_buttons.append(self.text_box)

        for name, on_clicked in self.current_algorithm.buttons:
            algorithm_button = self.control_panel.add_button(name, "")
            algorithm_button.clicked.connect(self.on_click_algorithm)
            algorithm_button.clicked.connect(on_clicked)
            self.codes_buttons.append(algorithm_button)

    def on_click_algorithm(self):
        self.current_algorithm.value = self.text_box.text()
        self.text_box.clear()

    def on_click_code(self, index):
        QDesktopServices.openUrl(self.current_algorithm.codes[index].url)

    def on_change_algorithm(self, index):
        self.set_algorithm(index)
        pass

    def set_algorithm(self, index):
        self.current_index = index
        self.current_algorithm = self.algorithms[index]
        self.reset()

    def show_description(self):
        self.center.clear_widget()
        self.bottom.set_text(self.current_algorithm.description)

    def reset(self):
        self.setup_control_panel()
        self.show_description()
        pass