#!/usr/bin/env bash
set -euo pipefail

# This script replaces the buggy implementation with a fixed version
# that properly allocates memory, reverses the string, and frees memory

cat > src/buggy.c << 'EOF'
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * Function to reverse a string
 * 
 * This function takes a string as input and returns
 * a new string with the characters in reverse order.
 * 
 * @param input The string to reverse
 * @return A pointer to the reversed string
 */
char* reverse_string(const char* input) {
    int length = strlen(input);
    
    // Allocate memory for the reversed string (including null terminator)
    char* reversed = (char*)malloc((length + 1) * sizeof(char));
    
    // Check if memory allocation was successful
    if (reversed == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    
    int i, j;
    
    // Copy characters in reverse order
    for (i = 0, j = length - 1; j >= 0; i++, j--) {
        reversed[i] = input[j];
    }
    
    // Add null terminator
    reversed[length] = '\0';
    
    return reversed;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <string>\n", argv[0]);
        return 1;
    }
    
    char* input = argv[1];
    char* result = reverse_string(input);
    
    printf("%s\n", result);
    
    // Free the allocated memory
    free(result);
    
    return 0;
}
EOF

echo "Fixed implementation written to src/buggy.c"
