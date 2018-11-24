CC = ghc
SRC = src
LIB = $(SRC)/lib
DIST = dist/linux

all:
	make -s alfred
	make -s clean

# Directives
alfred:
	[ -d $(DIST) ] || mkdir -vp $(DIST)
	$(CC) -o $(DIST)/alfred $(SRC)/Main $(LIB)/*.hs

# Clean (Change this $(OS))
clean:
	find . -name "*.o"  -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.hi" -type f -print0 | xargs -0 /bin/rm -f
