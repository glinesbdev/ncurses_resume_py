SRC = ./src
CC := $(shell command -v python3)

all: ${SRC}
	@${CC} ${SRC}

PHONY: all
