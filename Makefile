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
CCCFLAGS=--name $(EXE)-$(VERSION) --paths $(LIB) --distpath $(DIST) --workpath $(BUILD)
CCDFLAGS=--add-data $(LIB)/lexer.py:. --add-data $(LIB)/nodes.py:. --add-data $(LIB)/symbols.py:.

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

.PHONY: test-bin test-cli
test-bin: $(BINARY) $(EXAMPLE)/*
	for filetest in $^; do \
		echo "Example: $${filetest}"; ./$< $${filetest}; echo; done

test-cli: $(EXAMPLE)/*
	for filetest in $^; do \
		echo "Example: $${filetest}"; $(EXE) $${filetest}; echo; done

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
