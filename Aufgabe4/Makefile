all: build/A04_Clara_Sondermann_Enno_Wellmann.pdf 

build/A04_Clara_Sondermann_Enno_Wellmann.pdf: A04_Clara_Sondermann_Enno_Wellmann.tex ../header.tex rechnerei.py build/plot.pdf | build
	lualatex --output-directory=build --halt-on-error A04_Clara_Sondermann_Enno_Wellmann.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error A04_Clara_Sondermann_Enno_Wellmann.tex


build/plot.pdf: plotting.py ../matplotlibrc ../header-matplotlib.tex | build
	# so that matplotlib can find the tex header when running
	# LaTeX in the tmp directory
	# and set the matplotlibrc
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotting.py

build:
	mkdir -p build

rechnerei.py:
	python rechnerei.py

clean:
	rm -rf build