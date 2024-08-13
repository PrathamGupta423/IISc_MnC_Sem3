CXX = g++
CXXFLAGS = -fPIC -shared -std=c++11 -Wall -g -O3 
LDFLAGS = -shared

all: libarbit.so

libarbit.so: Arbit.o
	$(CXX) $(CXXFLAGS) -o libarbit.so Arbit.o

Arbit.o: Arbit.cpp Arbit.h
	$(CXX) $(CXXFLAGS) -c Arbit.cpp

clean:
	rm -f libarbit.so *.o