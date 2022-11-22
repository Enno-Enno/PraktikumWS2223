all: build/v207_Clara_Sondermann_Enno_Wellmann.pdf
	
build/v207_Clara_Sondermann_Enno_Wellmann.pdf:
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \