all:
#	$(MAKE) -C Aufgabe1
#	$(MAKE) -C Aufgabe2
#	$(MAKE) -C Aufgabe4
#	$(MAKE) -C 01_v207
	$(MAKE) -C 02_v206
	$(MAKE) -C 03_v303
	$(MAKE) -C 04_v308


clean:
#	$(MAKE) -C Aufgabe1 clean
#	$(MAKE) -C Aufgabe2 clean
#	$(MAKE) -C Aufgabe4 clean
#	$(MAKE) -C 01_v207 clean
	$(MAKE) -C 02_v206 clean
	$(MAKE) -C 03_v303 clean
	$(MAKE) -C 04_v308 clean

.PHONY: all clean
