#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "\\HelloWorld";
    int length = strlen(str);

    printf("Original string: %s\n", str);

    printf("AND operation with 127:\n");
    for (int i = 0; i < length; i++) {
        str[i] = str[i] & 127;
        printf("%c", str[i]);
    }
    printf("\n");

    printf("XOR operation with 127:\n");
    for (int i = 0; i < length; i++) {
        str[i] = str[i] ^ 127;
        printf("%c", str[i]);
    }
    printf("\n");

    printf("Press Enter to exit...");
    getchar(); // Wait for user input before exiting
    return 0;
}