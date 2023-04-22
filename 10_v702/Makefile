all: build/v702_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v702_Enno_Wellmann_Clara_Sondermann.pdf: v702_Enno_Wellmann_Clara_Sondermann.tex build/c02_vanadium_log.pdf build/c02_vanadium_err.pdf build/c03_silber1_log.pdf build/c04_silber2_log.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/c02_vanadium_log.pdf: c01_nulleffekt.py c02_vanadium.py ../matplotlibrc ../header-matplotlib.tex messung_c02_vanadium.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c02_vanadium.py

build/c02_vanadium_err.pdf: c01_nulleffekt.py c02_vanadium.py ../matplotlibrc ../header-matplotlib.tex messung_c02_vanadium.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c02_vanadium.py

build/c03_silber1_log.pdf: c01_nulleffekt.py c03_silber1.py ../matplotlibrc ../header-matplotlib.tex messung_c03_silber1.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c03_silber1.py

build/c03_silber1_err.pdf: c01_nulleffekt.py c03_silber1.py ../matplotlibrc ../header-matplotlib.tex messung_c03_silber1.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c03_silber1.py

build/c04_silber2_log.pdf: c01_nulleffekt.py c04_silber2.py ../matplotlibrc ../header-matplotlib.tex messung_c04_silber2.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python c04_silber2.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean