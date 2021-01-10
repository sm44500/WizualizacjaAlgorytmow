class Styles:
	main_background = """background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
	stop:0.0625 rgba(80, 80, 80, 255), stop:1 rgba(70, 70, 70, 255));"""

	standard_background = """background-color: rgb(187, 187, 187)"""

	description_background = """
		background-color: rgba(0, 0, 15, 255);
		color: #cccccc;
		font: bold;
		font-size: 32px;
		font-family: Arial;
	"""

	standard_tooltip = """
	QToolTip { 
		background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(210, 210, 210), stop:0.8 rgb(200, 200, 200), stop:1 rgb(190, 190, 190));
		color: black;
		font: bold;
		font-size: 15px;
		font-family: Arial;
		border: 1px solid black;
	}
	"""

	top_panel_option_background = """
		background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(150, 150, 150), stop:0.8 rgb(140, 140, 140), stop:1 rgb(130, 130, 130));
		font-family:Arial;
		font-size:24px;
	"""

	top_panel_background = """
	QComboBox {
		border: 0px solid black;
		border-radius: 0px;
		padding-left: 5px;
		padding-right: 5px;
		background-color: rgb(187, 187, 187);
	}
	
	QComboBox:editable {
		background: white;
	}
	
	QComboBox:on {
		background: gray;
	}
	
	QComboBox QAbstractItemView {
		border: 2px solid black;
		selection-background-color: lightgray;
	}
	"""

	right_panel_background = """
	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(100, 100, 100), stop:1 rgb(60, 60, 60));
	border-radius: 0px;
	"""

	button_background = """
	QPushButton {
		padding-left: 5px; padding-right: 5px; text-align: left;
		background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(150, 150, 150), stop:0.8 rgb(140, 140, 140), stop:1 rgb(130, 130, 130));
		border-radius: 0px;
	}
	QPushButton::hover {
		background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(190, 190, 190), stop:1 rgb(180, 180, 180));
	}
	""" + standard_tooltip

	settings_background = """
	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(100, 100, 100), stop:1 rgb(90, 90, 90));
	border-radius: 0px;
	"""

	welcome_background = """
	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(210, 210, 210), stop:1 rgb(150, 150, 150));
	border-radius: 0px;
	"""

	snapshot_button_background = button_background

	snapshot_button_background_clicked = """
	QPushButton {
		padding-left: 5px; padding-right: 5px; text-align: left;
		background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(190, 190, 190), stop:1 rgb(180, 180, 180));
		border-radius: 0px;
	}
	QPushButton::hover {
		background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(210, 210, 210), stop:1 rgb(190, 190, 190));
	}
	""" + standard_tooltip

	button_label = """
	color:rgb(0, 0, 0);
	background-color:rgba(0, 0, 0, 0);
	font-family:Arial;
	font-size:20px;
	"""

	label_background = """
	QLabel {
		background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(150, 150, 150), stop:0.8 rgb(140, 140, 140), stop:1 rgb(130, 130, 130));
		border-radius: 0px;
	}""" + standard_tooltip

	text_box_background = """
	QLineEdit {
		background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(180, 180, 180), stop:0.8 rgb(190, 190, 190), stop:1 rgb(200, 200, 200));
		border-radius: 0px;
	}""" + standard_tooltip

	slider_background = """
	QSlider::groove {
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(180, 180, 180), stop:1 rgb(200, 200, 200));
	}
	QSlider::handle {
		background: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 rgb(180, 180, 180), stop:1 rgb(200, 200, 200));
		border: 2px solid rgb(100, 100, 100);
		width: 12px;
		margin: 2px;
	}
	""" + standard_tooltip