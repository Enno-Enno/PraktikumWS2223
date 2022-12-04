all: build/v206_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v206_Clara_Sondermann_Enno_Wellmann.pdf: v206_Clara_Sondermann_Enno_Wellmann.tex FORCE build/plot_temp_verlauf.pdf build/plot_ausgleich_1.pdf build/plot_ausgleich_2.pdf build/plot_ausgleich_3.pdf build/plot_verdampfungswaerme.pdf | build
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

build/plot_ausgleich_1.pdf: plot_ausgleich_1.py ../matplotlibrc ../header-matplotlib.tex messdaten.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot_ausgleich_1.py

build/plot_ausgleich_2.pdf: plot_ausgleich_2.py ../matplotlibrc ../header-matplotlib.tex messdaten.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot_ausgleich_2.py

build/plot_ausgleich_3.pdf: plot_ausgleich_3.py ../matplotlibrc ../header-matplotlib.tex messdaten.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot_ausgleich_3.py

build/plot_verdampfungswaerme.pdf: plot_verdampfungswaerme.py ../matplotlibrc ../header-matplotlib.tex messdaten.txt| build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot_verdampfungswaerme.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean