all: build/v303_Clara_Sondermann_Enno_Wellmann.pdf  #build/B03_12_Spulenpaar.pdf build/B01_Hysteresekurve.pdf build/B03_24_Spulenpaar.pdf
	
build/v303_Clara_Sondermann_Enno_Wellmann.pdf: v308_Clara_Sondermann_Enno_Wellmann.tex FORCE build/B03_innen_Spulenpaar.pdf | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<



build/B01_Hysteresekurve.pdf: B01_hysterese.py ../matplotlibrc ../header-matplotlib.tex messdaten/Hysterese_kurve/0_neukurve.txt messdaten/Hysterese_kurve/A_zurück.txt messdaten/Hysterese_kurve/B_negativ.txt messdaten/Hysterese_kurve/C_zurück.txt messdaten/Hysterese_kurve/D_wieder_hoch.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python B01_hysterese.py
 
build/B03_innen_Spulenpaar.pdf: B03_Spulenpaar.py ../matplotlibrc ../header-matplotlib.tex messdaten/Hysterese_kurve/0_neukurve.txt messdaten/Hysterese_kurve/A_zurück.txt messdaten/Hysterese_kurve/B_negativ.txt messdaten/Hysterese_kurve/C_zurück.txt messdaten/Hysterese_kurve/D_wieder_hoch.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python B03_Spulenpaar.py




build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean