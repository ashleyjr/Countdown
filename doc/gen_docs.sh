latex -output-format=pdf Countdown.tex
cd ..
rm -rf html
rm -rf latex
doxygen CountdownOnline.py
cd latex
make
cd ..
cp latex/refman.pdf doc/CountdownOnline.pdf
rm -rf html
rm -rf latex
doxygen CountdownTrain.py
cd latex
make
cd ..
cp latex/refman.pdf doc/CountdownTrain.pdf
rm -rf html
rm -rf latex
