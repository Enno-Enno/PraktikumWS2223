all: build/v504_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v504_Enno_Wellmann_Clara_Sondermann.pdf: v504_Enno_Wellmann_Clara_Sondermann.tex build/C01_plot.pdf build/C02_plot.pdf build/C03_plot.pdf build/C04_plot.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/C01_plot.pdf: C01_Kennlinie.py ../matplotlibrc ../header-matplotlib.tex C01_Kennlinie.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C01_Kennlinie.py

build/C02_plot.pdf: C02_Kennlinie.py ../matplotlibrc ../header-matplotlib.tex C02_Kennlinie.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02_Kennlinie.py
	
build/C03_plot.pdf: C03_Kennlinie.py ../matplotlibrc ../header-matplotlib.tex C03_Kennlinie.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C03_Kennlinie.py

build/C04_plot.pdf: C04_Anlauf.py ../matplotlibrc ../header-matplotlib.tex C04_Anlauf.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C04_Anlauf.py


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean