all: build/v206_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v206_Clara_Sondermann_Enno_Wellmann.pdf: v206_Clara_Sondermann_Enno_Wellmann.tex FORCE build/plot_temp_verlauf.pdf | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<
	
build/plot_temp_verlauf.pdf: plot_temp_verlauf.py ../matplotlibrc ../header-matplotlib.tex messdaten.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot_temp_verlauf.py
	

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean