all: build/Aufgabe_1.pdf

build/Aufgabe_1.pdf: build/plot.pdf Aufgabe_1.tex | build
	lualatex --output-directory=build --halt-on-error Aufgabe_1.tex

build/plot.pdf: Graphik.py | build
	python Graphik.py

build:
	mkdir -p build

clean:
	rm -r build