CC=pyinstaller
OPTS=--onefile --noconfirm --clean --log-level=WARN

MAIN=main

SRC=src
DIST=dist
BUILD=build

ifeq ($(VIRTUAL_ENV),)
	BUILD=$(info You should activate the build virtual enviroment)
	CONF-INST=virtualenv
else
	CONF-INST=pyinstaller
	BUILD-CMD=$(info Building the program...) $(CC) $(OPTS) $(SRC)/$(MAIN).py
endif

all:
	make -s configure
	make -s purge
	make -s build
	make -s clean

configure:
	$(info Running configuration...)
	$(if $(shell which $(CONF-INST)),$(info - $(CONF-INST) found!),$(shell pip3 install $(CONF-INST)))
	
purge:
	rm -rf $(DIST)

build:
	$(BUILD-CMD)

clean:
	rm -f $(MAIN).spec `find $(SRC) -name '*.pyc'`
	rm -rf $(BUILD) `find $(SRC) -name '__pycache__'`