EXE=alfred

SRC=src
LIB=lib
DIST=dist
BUILD=build
EXAMPLE=example

VERSION=$(shell cat VERSION)
BINARY=$(DIST)/$(EXE)-$(VERSION)

CC=pyinstaller
CCXFLAGS=--onefile --clean
CCDFLAGS=--add-data $(LIB)/lexer.py:. --add-data $(LIB)/nodes.py:.
CCCFLAGS=--name $(EXE)-$(VERSION) --paths $(LIB) --distpath $(DIST) --workpath $(BUILD)

.PHONY: all
all: $(BINARY)

$(BINARY): $(SRC)/$(EXE).py
	$(CC) $(CCCFLAGS) $(CCDFLAGS) $(CCXFLAGS) $<

.PHONY: install
install: setup.py
	python $< $@

.PHONY: uninstall
uninstall: setup.py
	pip $@ --yes $(EXE)

.PHONY: test
test: $(BINARY)
	./$< $(EXAMPLE)/holamundo.alf
	./$< $(EXAMPLE)/escribe.alf

.PHONY: clean drop purge mrproper
clean:
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.egg" -delete
	find . -type f -name "$(EXE).spec" -delete
	find . -path "./$(BUILD)/*" -exec rm -rf {} +
	find . -type d -name "$(EXE).egg-info" -exec rm -rf {} +
	find . -type d -name "__pycache__" ! -path "./venv/*" -exec rm -rf {} +
purge: clean
	find . -path "./$(DIST)/*" -exec rm -rf {} +
mrproper: purge
