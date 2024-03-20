SRC = ./src
CC := $(shell command -v python3)

.PHONY: all

all:
	@${CC} ${SRC}