all: build/v601_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v601_Enno_Wellmann_Clara_Sondermann.pdf: v601_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
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

build/C02_rechteck_beidseitig_links.pdf build/C02_rechteck_beidseitig_rechts.pdf: C00_umrechnung_rechteck_beidseitig.py C02_rechteck_beidseitig.py ../matplotlibrc ../header-matplotlib.tex messdaten/rechteck_beidseitig.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02_rechteck_beidseitig.py

build/C02_kreis_beidseitig_links.pdf build/C02_kreis_beidseitig_rechts.pdf: C00_umrechnung_kreis_beidseitig.py C02_kreis_beidseitig.py ../matplotlibrc ../header-matplotlib.tex messdaten/kreis_beidseitig.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02_kreis_beidseitig.py


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean