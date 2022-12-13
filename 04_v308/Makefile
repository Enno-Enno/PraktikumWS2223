all: build/v303_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v303_Clara_Sondermann_Enno_Wellmann.pdf: v308_Clara_Sondermann_Enno_Wellmann.tex FORCE | build
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