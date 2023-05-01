all: build/v504_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v504_Enno_Wellmann_Clara_Sondermann.pdf: v504_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

# build/c01_reflexion.pdf: c01_reflexion.py ../matplotlibrc ../header-matplotlib.tex messung_1_reflexion.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c01_reflexion.py


build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean