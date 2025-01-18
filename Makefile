LDFLAGS = -lraylib

all: terminal

terminal: terminal.c
	${CC} -o $@ $< ${LDFLAGS}

clean:
	rm terminal

.PHONY: all clean
