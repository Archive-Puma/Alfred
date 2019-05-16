EXE=alfred

SRC=src
LIB=lib
DIST=dist
TEST=test
BUILD=build

CC=pyinstaller
CCXFLAGS=--onefile --clean
CCDFLAGS=--add-data $(LIB)/lexer.py:.
CCCFLAGS=--name $(EXE) --paths $(LIB) --distpath $(DIST) --workpath $(BUILD)

.PHONY: all
all: $(DIST)/$(EXE)

$(DIST)/$(EXE): $(SRC)/$(EXE).py
	$(CC) $(CCCFLAGS) $(CCDFLAGS) $(CCXFLAGS) $<

.PHONY: test
test: $(DIST)/$(EXE)
	./$< $(TEST)/helloworld.alf

.PHONY: clean drop purge mrproper
clean:
	rm -rf $(BUILD)/*
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name "$(EXE).spec" -delete
purge: clean
	find $(DIST) -name $(EXE) -delete
mrproper: purge
