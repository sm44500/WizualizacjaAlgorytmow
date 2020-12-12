rm -rv ./dist/*
pyinstaller --clean -p ./WizualizacjaAlgorytmow/ -F  WizualizacjaAlgorytmow/WizualizacjaAlgorytmow.py
cp -rv ./WizualizacjaAlgorytmow/Algorithms ./dist/
cp -rv ./WizualizacjaAlgorytmow/Resources ./dist/