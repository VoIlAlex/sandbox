main: proc_2.o proc_1.o
	- gcc proc_1.o -o proc_1.exe
	- gcc proc_2.o -o proc_2.exe
proc_1.o: proc_1.c
	- gcc -c proc_1.c
proc_2.o: proc_2.c
	- gcc -c proc_2.c
clear:
	rm -f proc_1.o proc_1.exe
	rm -f proc_2.o proc_2.exe