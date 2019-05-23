EXE=alfred

SRC=src
LIB=lib
DIST=dist
DOCS=docs
BUILD=build
EXAMPLE=example

VERSION=$(shell cat VERSION)

ifeq ($(OS),Windows_NT)
	DELIMITER:=;
	BROWSER:=start
	KERNEL:=Windows
	ARCHITECTURE:=$(shell echo $(PROCESSOR_ARCHITECTURE) | tr A-Z a-z)

	include Makefile.Windows
else
	DELIMITER:=:
	BROWSER:=sensible-browser
	KERNEL:=$(shell uname -s)
	ARCHITECTURE:=$(shell uname -p)

	ifeq ($(KERNEL),Linux)
		include Makefile.Linux
	endif
	ifeq ($(KERNEL),Darwin)

	endif
endif

include Makefile.Docs
BINARY=$(EXE)-$(VERSION)-$(KERNEL)-$(ARCHITECTURE)

CC=pyinstaller
CCOPTS=--onefile --clean
CCDIRS=--distpath $(DIST) --workpath $(BUILD) --paths $(LIB)
CCFILES=--name $(BINARY) --add-data "VERSION$(DELIMITER)."

.PHONY:build
build: $(SRC)/$(EXE).py
	$(CC) $(CCOPTS) $(CCDIRS) $(CCFILES) $<

.PHONY: install
install: setup.py
	python $< $@

.PHONY: uninstall
uninstall:
	pip $@ --yes $(EXE)-lang
