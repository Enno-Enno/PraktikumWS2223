all: build/v701_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v701_Enno_Wellmann_Clara_Sondermann.pdf: v701_Enno_Wellmann_Clara_Sondermann.tex build/reichweite_6cm_rate.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/reichweite_6cm_rate.pdf: reichweite_6cm.py ../matplotlibrc ../header-matplotlib.tex messungen/reichweite_6cm.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python reichweite_6cm.py
# 
# build/reichweite_6cm_ladungszahl.pdf: reichweite_6cm.py ../matplotlibrc ../header-matplotlib.tex messungen/reichweite_6cm.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python reichweite_6cm.py



build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean