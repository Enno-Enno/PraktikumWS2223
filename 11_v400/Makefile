all: build/v400_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v400_Enno_Wellmann_Clara_Sondermann.pdf: v400_Enno_Wellmann_Clara_Sondermann.tex build/c01_reflexion.pdf build/c02_brechung.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/c01_reflexion.pdf: c01_reflexion.py ../matplotlibrc ../header-matplotlib.tex messung_1_reflexion.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c01_reflexion.py

build/c02_brechung.pdf: c02_brechung.py ../matplotlibrc ../header-matplotlib.tex messung_2_brechung.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c02_brechung.py


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean