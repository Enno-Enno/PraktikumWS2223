all: build/v353_Enno_Wellmann_Clara_Sondermann.pdf  
	
build/v353_Enno_Wellmann_Clara_Sondermann.pdf: v353_Enno_Wellmann_Clara_Sondermann.tex FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<






build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean