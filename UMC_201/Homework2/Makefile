CC=gcc

all: hw2.o dict.o
	$(CC) -o hw2 hw2.o dict.o

hw2.o: hw2.c dict.h
	$(CC) -c hw2.c

dict.o: dict.c dict.h
	$(CC) -c -O3 dict.c
 
clean:
	rm hw2 hw2.o dict.o
