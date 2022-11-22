all: build/v207_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v207_Clara_Sondermann_Enno_Wellmann.pdf: v207_Clara_Sondermann_Enno_Wellmann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<
	
build/plot.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex Messdaten.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
	

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean