class Styles:
	main_background = """background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
	stop:0.0625 rgba(80, 80, 80, 255), stop:1 rgba(70, 70, 70, 255));"""

	standard_background = """background-color: rgb(187, 187, 187)"""

	description_background = """background-color: rgba(187, 187, 187, 200)"""

	top_panel_background = """
	QComboBox {
		border: 0px solid black;
		border-radius: 0px;
		padding-left: 5px;
		padding-right: 5px;
		background-color: rgb(187, 187, 187)
	}

	QComboBox:!editable:on, QComboBox::drop-down:editable:on {
		background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #D3D3D3, stop: 0.4 #D8D8D8, stop: 0.5 #DDDDDD,
		stop: 1.0 #E1E1E1);
	}
	"""

	right_panel_background = """
	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(100, 100, 100), stop:1 rgb(60, 60, 60));
	border-radius: 0px;
	"""

	button_background = """
	QPushButton {
		padding-left: 5px; padding-right: 5px; text-align: left;
		background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(160, 160, 160), stop:1 rgb(150, 150, 150));
		border-radius: 0px;
	}
	QPushButton::hover {
		background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(190, 190, 190), stop:1 rgb(180, 180, 180));
	}
	"""

	snapshot_button_background = button_background

	button_label = """
	color:rgb(0, 0, 0);
	background-color:rgba(0, 0, 0, 0);
	font-family:Arial;
	font-size:20px;
	"""

	label_background = """
	background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(160, 160, 160), stop:1 rgb(150, 150, 150));
	border-radius: 0px;
	"""

	text_box_background = """
	background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(180, 180, 180), stop:1 rgb(200, 200, 200));
	border-radius: 0px;
	"""

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
	"""