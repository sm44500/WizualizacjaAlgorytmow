import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from WelcomeWindow import WelcomeWindow


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("fusion")
	main_window = MainWindow()
	#main_window.show()
	main_window.showMaximized()
	welcome_window = WelcomeWindow()
	welcome_window.show()
	sys.exit(app.exec_())		


