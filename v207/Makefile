all: build/v207_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v207_Clara_Sondermann_Enno_Wellmann.pdf: v207_Clara_Sondermann_Enno_Wellmann.tex FORCE build/Messreihe3.pdf | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<
	
build/Messreihe3.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex Messdaten_grKu_steigendeTemp.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
	

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean