all: build/v353_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v353_Enno_Wellmann_Clara_Sondermann.pdf: v353_Enno_Wellmann_Clara_Sondermann.tex build/C01_aufg_a.pdf build/C02_aufg_b.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<


build/C01_aufg_a.pdf: C01_aufg_a.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C01_aufg_a.py

build/C02_aufg_b.pdf: C02b_aufg_b.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt C02_aufg_b_c.py | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02b_aufg_b.py

build/C02_aufg_c.pdf: C02c_aufg_c.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt C02_aufg_b_c.py | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02c_aufg_c.py




build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean