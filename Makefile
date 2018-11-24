CC		= ghc
SRC		= src
DIST	= dist
NAME	= alfred
LIB		= $(SRC)/core
BUILD	= $(DIST)/build/$(NAME)

all:
	make -s build
	make -s configure
	make -s clean

configure:
	[ -d $(BUILD) ] || mkdir -vp $(BUILD)

build:
	$(CC) -o $(BUILD)/$(NAME) $(SRC)/Main $(LIB)/*.hs

# FIXME: (Change this $(OS))
clean:
	rm -rf $(DIST)/setup-config
	rm -rf $(BUILD)/$(NAME)-tmp
	rm -rf $(DIST)/build/autogen
	rm -rf $(DIST)/package.conf.inplace
	find . -name "*.a" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.o"  -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.hi" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.so" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.dyn_o" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.dyn_hi" -type f -print0 | xargs -0 /bin/rm -f
