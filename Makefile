obj = words.o  
CFLAGS = 

all:wordnet matrix marketformat

wordnet:$(obj)
	g++ -o words $(obj) 
matrix:matrix.o
	g++ -o matrix matrix.o
marketformat:marketformat.o
	g++ -o marketformat marketformat.o
.PHONY : clean
clean :
	-rm words $(obj) matrix matrix.o marketformat marketformat.o

