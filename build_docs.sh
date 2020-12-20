rm -rv ./docs/*
pushd ./WizualizacjaAlgorytmow
python3 -m pdoc --output-dir ../docs --html . 
popd
mv -v ./docs/WizualizacjaAlgorytmow/* ./docs
rmdir ./docs/WizualizacjaAlgorytmow