CC = gcc
CFLAGS = -Wall -Wextra -g
SRC_DIR = src
TARGET = reverse

all: $(TARGET)

$(TARGET): $(SRC_DIR)/buggy.c
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC_DIR)/buggy.c

clean:
	rm -f $(TARGET)

.PHONY: all clean
