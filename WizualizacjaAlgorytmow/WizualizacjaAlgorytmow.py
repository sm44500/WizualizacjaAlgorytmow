import sys
from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("fusion")
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
