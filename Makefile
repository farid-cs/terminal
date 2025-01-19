CFLAGS = -std=c99 -pedantic -Wall -Wextra
LDFLAGS = -lraylib

all: terminal

terminal: terminal.c
	${CC} ${CFLAGS} -o $@ $< ${LDFLAGS}

clean:
	rm terminal

.PHONY: all clean
