all: build/loesung2.pdf

build/loesung2.pdf: loesung2.tex | build
	lualatex --output-directory=build --interaction=batchmode --halt-on-error loesung2.tex
	lualatex --output-directory=build --interaction=batchmode --halt-on-error loesung2.tex

build:
	mkdir -p build

clean:
	rm -rf build