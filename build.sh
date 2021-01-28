rm -rv ./dist/*
pyinstaller --clean -p ./WizualizacjaAlgorytmow/ -F --icon=./WizualizacjaAlgorytmow/Resources/Icons/app_icon.ico WizualizacjaAlgorytmow/WizualizacjaAlgorytmow.py
cp -rv ./WizualizacjaAlgorytmow/Algorithms ./dist/
cp -rv ./WizualizacjaAlgorytmow/Resources ./dist/