all: build/v303_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v303_Clara_Sondermann_Enno_Wellmann.pdf: v303_Clara_Sondermann_Enno_Wellmann.tex FORCE build/B01_ausgleichsplot.pdf build/B02_ausgleichsplot.pdf | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<
	
#build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex Messdaten_grKu_steigendeTemp.txt| build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
#
#build/Messreihe3.pdf: Messreihe3.py ../matplotlibrc ../header-matplotlib.tex Messdaten_grKu_steigendeTemp.txt| build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python Messreihe3.py

build/B01_ausgleichsplot.pdf: B01_ausgleichsplot.py ../matplotlibrc ../header-matplotlib.tex B01_messdaten.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python B01_ausgleichsplot.py

build/B02_ausgleichsplot.pdf: B02_ausgleichsplot.py ../matplotlibrc ../header-matplotlib.tex B02_messdaten.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python B02_ausgleichsplot.py




build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean