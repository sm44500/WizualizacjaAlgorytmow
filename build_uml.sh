pushd ./WizualizacjaAlgorytmow
pyreverse -A -o pdf -p WizualizacjaAlgorytmow \
  ./*.py \
  ./Widgets/* \
  ./AlgorithmsLogic/*
mv classes_WizualizacjaAlgorytmow.pdf ..
mv packages_WizualizacjaAlgorytmow.pdf ..
popd