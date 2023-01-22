all: build/v103_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v103_Enno_Wellmann_Clara_Sondermann.pdf: v103_Enno_Wellmann_Clara_Sondermann.tex build/C02_rechteck_einseitig.pdf build/C02_kreis_einseitig.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/C02_rechteck_einseitig.pdf: C00_umrechnung_rechteck_einseitig.py C02_rechteck_einseitig.py ../matplotlibrc ../header-matplotlib.tex messdaten/rechteck_einseitig.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02_rechteck_einseitig.py

build/C02_kreis_einseitig.pdf: C00_umrechnung_kreis_einseitig.py C02_kreis_einseitig.py ../matplotlibrc ../header-matplotlib.tex messdaten/kreis_einseitig.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02_kreis_einseitig.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean