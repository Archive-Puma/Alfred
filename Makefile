EXE=alfred

SRC=src
LIB=lib
DIST=dist
DOCS=docs
BUILD=build
EXAMPLE=example

VERSION=$(shell cat VERSION)

ifeq ($(OS),Windows_NT)

else
	BROWSER:=sensible-browser
	KERNEL:=$(shell uname -s)
	ARCHITECTURE:=$(shell uname -p)
	VERSION:=$(VERSION)-$(KERNEL)

	ifeq ($(KERNEL),Linux)
		include Makefile.Linux
	endif
	ifeq ($(KERNEL),Darwin)

	endif
endif

include Makefile.Docs
BINARY=$(DIST)/$(EXE)-$(VERSION)-$(ARCHITECTURE)
