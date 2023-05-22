all: build/v701_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v701_Enno_Wellmann_Clara_Sondermann.pdf: v701_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

# build/teil1_rate.pdf: teil1.py ../matplotlibrc ../header-matplotlib.tex messungen/teil1.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python teil1.py
# 
# build/teil1_ladungszahl.pdf: teil1.py ../matplotlibrc ../header-matplotlib.tex messungen/teil1.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python teil1.py



build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean