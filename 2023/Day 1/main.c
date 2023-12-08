#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int findDigit(char* line, int startIdx, int increment) {
    while (line[startIdx] != '\0') {
        if (isdigit((unsigned char)line[startIdx])) {
            return line[startIdx] - '0';
        }
        startIdx += increment;
    }
    return -1;  // Return -1 if no digit is found
}

int main() {
    FILE* ptr;
    char buffer[256];
    char** lines = NULL;
    size_t lineCount = 0;

    ptr = fopen("input", "r");

    int sum = 0;

    while (fgets(buffer, sizeof(buffer), ptr) != NULL) {
        buffer[strcspn(buffer, "\n")] = '\0';
        char* new_line = strdup(buffer);
        lines = (char **)realloc(lines, (lineCount + 1) * sizeof(char *));
        lines[lineCount++] = new_line;

        char* line = lines[lineCount - 1];
        size_t line_length = strlen(line);

        int first_digit = findDigit(line, 0, 1);
        int last_digit = findDigit(line, line_length - 1, -1);

        if (first_digit != -1 && last_digit != -1) {
            int two_digit_number = first_digit * 10 + last_digit;
            sum += two_digit_number;
        } else {
            printf("Line %zu: Invalid format\n", lineCount);
        }
    }

    printf("Total sum of calibration values: %d\n", sum);

    for (size_t i = 0; i < lineCount; i++) {
        free(lines[i]);
    }
    free(lines);

    fclose(ptr);
    return 0;
}
