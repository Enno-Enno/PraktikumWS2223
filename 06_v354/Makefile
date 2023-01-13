all: build/v354_Enno_Wellmann_Clara_Sondermann.pdf
	
build/v354_Enno_Wellmann_Clara_Sondermann.pdf: v354_Enno_Wellmann_Clara_Sondermann.tex build/C01_a.pdf FORCE | build
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	  $<

build/C01_a.pdf: C00_umrechnungen.py C01_a.py ../matplotlibrc ../header-matplotlib.tex messdaten/ampl_ged_schw_raw.txt | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C01_a.py

# build/C01_a_plot.pdf
# messdaten/ampl_ged_schw_raw.txt
# C00_umrechnungen.py

# build/plot_a.pdf.pdf: C01a_aufg_a_plot.py plot_a.pdf.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C01a_aufg_a_plot.py

# build/C02_aufg_b.pdf: C02b_aufg_b.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt C02_aufg_b_c.py | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02b_aufg_b.py

# build/C02_aufg_c.pdf: C02c_aufg_c.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt C02_aufg_b_c.py | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02c_aufg_c.py

# build/C02_aufg_d.pdf: C02d_aufg_d.py ../matplotlibrc ../header-matplotlib.tex messdaten/A/a_in_kaestchen.txt C02_aufg_b_c.py | build
# 	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python C02d_aufg_d.py




build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean