
# Variables to control Makefile operation

CC = g++
CFLAGS = -Wall -g

valid-anagram: valid-anagram.o
	$(CC) $(CFLAGS) -o valid-anagram valid-anagram.o

valid-anagram.o: valid-anagram.cpp
	$(CC) $(CFLAGS) -c valid-anagram.cpp

clean:
	rm -rf valid-anagram valid-anagram.o
