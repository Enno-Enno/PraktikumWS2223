all: build/A04_Clara_Sondermann_Enno_Wellmann.pdf

build/A04_Clara_Sondermann_Enno_Wellmann.pdf: A04_Clara_Sondermann_Enno_Wellmann.tex ../header.tex | build
	lualatex --output-directory=build --halt-on-error A04_Clara_Sondermann_Enno_Wellmann.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error A04_Clara_Sondermann_Enno_Wellmann.tex

build:
	mkdir -p build

clean:
	rm -rf build