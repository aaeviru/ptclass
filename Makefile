obj = words.o  
CC = g++
CFLAGS = -l sqlite3

all:wordnet matrix marketformat acp

wordnet:$(obj)
	g++ -o words $(obj) 
matrix:matrix.o
	g++ -o matrix matrix.o
marketformat:marketformat.o
	g++ -o marketformat marketformat.o
acp:acp.o ../wordnet/wordnet.o
	 $(CC) $(CFLAGS) $^ -o $@
.PHONY : clean
clean :
	-rm words $(obj) matrix matrix.o marketformat marketformat.o

