NAME := alfred

Dsrc := src
Dlib := lib
Ddist := dist
Dbuild := build
Dinclude := include

CC := g++
CFLAGS := -Wall
CINCLUDE := -I./$(Dinclude)

LIBS := $(wildcard $(Dlib)/*.cpp)
OBJS := $(patsubst $(Dlib)/%.cpp, $(Dbuild)/%.o, $(LIBS))

.PHONY: build
build: $(Ddist)/$(NAME)
	@true

$(Ddist)/$(NAME): $(Dsrc)/main.cpp $(OBJS)
	$(CC) $(CFLAGS) $(CINCLUDE) -o $@ $^

$(Dbuild)/%.o: $(Dlib)/%.cpp
	$(CC) $(CFLAGS) $(CINCLUDE) -o $@ -c $<

.PHONY: test
test: $(Ddist)/$(NAME)
	./$< test/prueba.alf

.PHONY: clean
clean:
	@rm $(Dbuild)/*

	
