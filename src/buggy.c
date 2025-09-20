#include <stdio.h>
#include <string.h>

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
    char* reversed;  // Uninitialized pointer - bug!
    int length = strlen(input);
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
    
    // Missing free() - memory leak!
    
    return 0;
}
