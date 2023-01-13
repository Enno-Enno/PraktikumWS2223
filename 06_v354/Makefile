all: build/v354_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v354_Enno_Wellmann_Clara_Sondermann.pdf: v354_Enno_Wellmann_Clara_Sondermann.tex build/C01_a.pdf build/C03_c_d.pdf build/C03_c_d_linear.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/C01_a.pdf: C00_umrechnungen.py C01_a.py ../matplotlibrc ../header-matplotlib.tex messdaten/ampl_ged_schw_raw.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C01_a.py

build/C03_c_d.pdf: C00_umrechnungen.py C03_c_d.py ../matplotlibrc ../header-matplotlib.tex messdaten/spannung_phase_raw.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C03_c_d.py

build/C03_c_d_linear.pdf: C00_umrechnungen.py C03_c_d.py ../matplotlibrc ../header-matplotlib.tex messdaten/spannung_phase_raw.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C03_c_d.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean