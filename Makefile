NAME := alfred
FILE := test.alf

Dsrc := src
Dlib := lib
Ddist := dist
Dtest := test
Dbuild := build
Dinclude := include

CC := g++
CLANG := clang++
CFLAGS := -std=c++17 -Wall
CINCLUDE := -I./$(Dinclude)

LIBS := $(wildcard $(Dlib)/*.cpp)
OBJS := $(patsubst $(Dlib)/%.cpp, $(Dbuild)/%.o, $(LIBS))

.PHONY: build
build: $(Ddist)/$(NAME)
	@true

.PHONY: clang
clang: $(Ddist)/$(NAME)-clang
	@true

$(Ddist)/$(NAME): $(Dsrc)/main.cpp $(OBJS)
	$(CC) $(CFLAGS) $(CINCLUDE) -o $@ $^

$(Ddist)/$(NAME)-clang: $(Dsrc)/main.cpp $(OBJS)
	$(CLANG) $(CFLAGS) $(CINCLUDE) -o $@ $^

$(Dbuild)/%.o: $(Dlib)/%.cpp
	$(CC) $(CFLAGS) $(CINCLUDE) -o $@ -c $<

.PHONY: zipunix
zipunix: $(Ddist)/$(NAME) $(Dtest)/$(FILE)
	cat $^ > $(Ddist)/$(NAME)-zipped

.PHONY: test
test: $(Ddist)/$(NAME)
	./$< -df $(Dtest)/$(FILE)

.PHONY: test-clang
test-clang: $(Ddist)/$(NAME)-clang
	./$< -f $(Dtest)/$(FILE)

.PHONY: clean
clean:
	@rm -f $(Dbuild)/* *.log

.PHONY: purge
purge: clean
	@rm -f $(Ddist)/*
