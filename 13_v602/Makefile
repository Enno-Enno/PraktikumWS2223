all: build/v602_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v602_Enno_Wellmann_Clara_Sondermann.pdf: v602_Enno_Wellmann_Clara_Sondermann.tex FORCE build/01_plot.pdf build/02_plot.pdf build/03_plot.pdf build/04_plot.pdf build/05_plot.pdf| build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/01_plot.pdf: 01_Bragg_Bedingung.py ../matplotlibrc ../header-matplotlib.tex v602_messungen/BraggBedingung.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python 01_Bragg_Bedingung.py

build/02_plot.pdf: 02_Spektrum_grob.py ../matplotlibrc ../header-matplotlib.tex v602_messungen/ohne_detail.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python 02_Spektrum_grob.py
	
build/03_plot.pdf: 03_spektrum_genau.py ../matplotlibrc ../header-matplotlib.tex v602_messungen/detail.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python 03_spektrum_genau.py

build/04_plot.pdf: 04_k_Kanten.py ../matplotlibrc ../header-matplotlib.tex v602_messungen/abs_brom.txt v602_messungen/abs_sr.txt  | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python 04_k_Kanten.py

build/05_plot.pdf: 05_rechenpython.py ../matplotlibrc ../header-matplotlib.tex  | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python 05_rechenpython.py


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean