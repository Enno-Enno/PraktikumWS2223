all: build/v703_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v703_Enno_Wellmann_Clara_Sondermann.pdf: v703_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

#build/01_plot.pdf: 01_Bragg_Bedingung.py ../matplotlibrc ../header-matplotlib.tex v602_messungen/BraggBedingung.txt | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python 01_Bragg_Bedingung.py



build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean