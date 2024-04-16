#include <stdio.h>

#define SIZE 3 // Size of the matrix

void transpose(int mat[SIZE][SIZE]) {
    int temp;
    for (int i = 0; i < SIZE; i++) {
        for (int j = i + 1; j < SIZE; j++) {
            // Swap the elements mat[i][j] and mat[j][i]
            temp = mat[i][j];
            mat[i][j] = mat[j][i];
            mat[j][i] = temp;
        }
    }
}

void displayMatrix(int mat[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int matrix[SIZE][SIZE];

    // Input the matrix
    printf("Enter the elements of the %dx%d matrix:\n", SIZE, SIZE);
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Display the original matrix
    printf("Original matrix:\n");
    displayMatrix(matrix);

    // Transpose the matrix
    transpose(matrix);

    // Display the transposed matrix
    printf("\nTransposed matrix:\n");
    displayMatrix(matrix);

    printf("Press Enter to exit...");
    getchar(); // Wait for user input before exiting
    return 0;
}
