all:
	$(MAKE) -C Aufgabe_1
	$(MAKE) -C Aufgabe2


clean:
	$(MAKE) -C Aufgabe_1 clean
	$(MAKE) -C Aufgabe2 clean

.PHONY: all clean
