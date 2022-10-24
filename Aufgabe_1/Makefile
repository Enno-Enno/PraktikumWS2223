all: build/A01_Clara_Sondermann_Enno_Wellmann.pdf

build/A01_Clara_Sondermann_Enno_Wellmann.pdf: build/plot.pdf A01_Clara_Sondermann_Enno_Wellmann.tex | build
	lualatex --output-directory=build --halt-on-error A01_Clara_Sondermann_Enno_Wellmann.tex

build/plot.pdf: Graphik.py | build
	python Graphik.py

build:
	mkdir -p build

clean:
	rm -r build