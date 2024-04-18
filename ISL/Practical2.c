#include <stdio.h>
#include <string.h>

int main() {
    int i, j, l, track;
    char a[20], c[20], d[20];

    printf("\n\t\tRAIL FENCE TECHNIQUE\n\n");
    printf("Enter the input string: ");
    fgets(a, sizeof(a), stdin);
    a[strcspn(a, "\n")] = '\0'; // Remove newline character

    // Basic input validation (check for empty string)
    if (strlen(a) == 0) {
        printf("Error: Input string cannot be empty.\n");
        return 1;
    }

    printf("Enter the number of tracks (positive integer): ");
    do {
        scanf("%d", &track);
        getchar(); // Consume newline character
    } while (track <= 0); // Repeat prompt if track is not positive

    l = strlen(a);

    /* Ciphering */
    for (i = 0, j = 0; i < l; i++) {
        if (i % track == 0)
            c[j++] = a[i];
    }
    for (i = 0; i < l; i++) {
        if (i % track != 0)
            c[j++] = a[i];
    }
    c[j] = '\0';

    printf("\nCipher text after applying rail fence: %s\n", c);

    /* Deciphering */
    int cycles = (l + track - 1) / track;
    int rows = track;
    int cols = cycles;
    int rail[cycles][track];

    // Fill rail with placeholders (0 for empty)
    for (i = 0; i < cycles; i++) {
        for (j = 0; j < track; j++) {
            rail[i][j] = 0;
        }
    }

    // Mark rail with positions where characters should be placed
    int pos = 0;
    for (i = 0; i < cycles; i++) {
        for (j = 0; j < track; j++) {
            if (j == 0 || j == track - 1) {
                rail[i][j] = pos++;
            }
        }
    }

    // Fill rail with characters from cipher text
    pos = 0;
    for (i = 0; i < cycles; i++) {
        for (j = 0; j < track; j++) {
            if (rail[i][j] != 0) {
                rail[i][j] = c[pos++];
            }
        }
    }

    // Read characters from rail
    pos = 0;
    int filled = 0; // Track filled positions
    for (i = 0; i < cycles; i++) {
        for (j = 0; j < track; j++) {
            // Check if position is not empty and increment filled counter
            if (rail[i][j] != 0) {
                d[pos++] = rail[i][j];
                filled++;
            }
            // Boundary check to avoid out-of-bounds access
            else if (pos >= l) {
                // Reached end of message, exit loop
                break;
            }
        }
    }

    // Add null terminator (considering potential empty positions)
    d[filled] = '\0';

    printf("Decrypted text: %s\n", a);

    return 0;
}