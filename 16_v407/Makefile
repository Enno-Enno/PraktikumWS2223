all: build/v407_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v407_Enno_Wellmann_Clara_Sondermann.pdf: v407_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/01_plot.pdf: C01_intensitaet.py ../matplotlibrc ../header-matplotlib.tex messungen/intensitaet.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C01_intensitaet.py
# 
# build/reichweite_6cm_energymax.pdf: reichweite_6cm.py ../matplotlibrc ../header-matplotlib.tex messungen/reichweite_6cm.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python reichweite_6cm.py
# 
# build/reichweite_7cm_rate.pdf: reichweite_7cm.py ../matplotlibrc ../header-matplotlib.tex messungen/reichweite_7cm.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python reichweite_7cm.py
# 
# build/reichweite_7cm_energymax.pdf: reichweite_7cm.py ../matplotlibrc ../header-matplotlib.tex messungen/reichweite_7cm.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python reichweite_7cm.py
# 
# build/statistik.pdf: statistik.py ../matplotlibrc ../header-matplotlib.tex messungen/statistik.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python statistik.py


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean