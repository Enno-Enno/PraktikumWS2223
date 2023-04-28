all: build/v400_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v400_Enno_Wellmann_Clara_Sondermann.pdf: v400_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

#build/c02_vanadium_log.pdf: c01_nulleffekt.py c02_vanadium.py ../matplotlibrc ../header-matplotlib.tex messung_c02_vanadium.txt | build
#	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c02_vanadium.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean