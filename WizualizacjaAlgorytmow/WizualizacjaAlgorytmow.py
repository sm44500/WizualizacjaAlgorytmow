import sys
from PyQt5.QtWidgets import QApplication

from MainApplication import MainApplication

if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("fusion")
	main_application = MainApplication()
	main_application.show()
	sys.exit(app.exec_())