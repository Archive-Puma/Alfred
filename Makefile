NAME=alfred

Dsrc=src
Dlib=lib
Ddist=dist

SRC=$(wildcard $(Dsrc)/*.cpp)
LIB=$(wildcard $(Dlib)/*.cpp)
OBJ=$(LIB:.cpp=.o)

CC=g++
CFLAGS=-Wall
CINCLUDE=-I./$(Dlib)

.PHONY: build
build: $(Ddist)/$(NAME)
	@true

$(Ddist)/$(NAME): $(SRC) $(OBJ)
	$(CC) $(CFLAGS) $(CINCLUDE) -o $@ $^

.PHONY: test
test: $(Ddist)/$(NAME)
	./$< test/prueba.alf

.PHONY: clean
clean:
	@rm $(OBJ)

	
