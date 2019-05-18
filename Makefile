EXE=alfred

SRC=src
LIB=lib
DIST=dist
BUILD=build
EXAMPLE=example

VERSION=$(shell cat VERSION)

ifeq ($(OS),Windows_NT)

else
	KERNEL:=$(shell uname -s)
	ARCHITECTURE:=$(shell uname -p)
	VERSION:=$(VERSION)-$(KERNEL)

	ifeq ($(KERNEL),Linux)
		include Makefile.Linux
	endif
	ifeq ($(KERNEL),Darwin)

	endif
endif

BINARY=$(DIST)/$(EXE)-$(VERSION)-$(ARCHITECTURE)
