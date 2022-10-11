all: build/plot.pdf


build/plot.pdf: Graphik.py | build
	python Graphik.py

build:
	mkdir -p build

clean:
	rm -r build