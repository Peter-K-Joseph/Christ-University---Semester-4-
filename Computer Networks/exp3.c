#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char getXORvalue(char divident, char divisor) {
    if (divident == '0' && divisor == '0' || divident == '1' && divisor == '1') {
        return '0';
    } else {
        return '1';
    }
}

int main() {
    char string[100], divisor[4], quotient[50], reminder[5], buffer;
    int err_pos, quotpos = 0;
    printf("Enter a string: ");
    fgets(string, 100, stdin);
    string[strlen(string) - 1] = '\0';
    printf("Enter a divisor: ");
    fgets(divisor, 4, stdin);
    divisor[strlen(divisor) - 1] = '\0';
    printf("Enter error position: ");
    scanf("%s", &buffer);
    scanf("%d", &err_pos);
    if (strlen(string) < 4) {
        printf("Error: String is too short.\n");
        return 0;
    }
    for (int i = 0 ; i < strlen(string)-3; i++) {
        reminder[0] = getXORvalue(string[i], divisor[0]);
        reminder[1] = getXORvalue(string[i+1], divisor[1]);
        reminder[2] = getXORvalue(string[i+2], divisor[2]);
        reminder[3] = getXORvalue(string[i+3], divisor[3]);
        reminder[4] = '\0';
        if (reminder[0] == '0') {
            quotient[quotpos] = '0';
        } else {
            quotient[quotpos] = '1';
        }
        printf("%c%c%c%c ^ '%c'%c'%c'%c' = %s\n", string[i], string[i+1], string[i+2], string[i+3], divisor[0], divisor[1], divisor[2], divisor[3], reminder);
        quotpos++;
    }
    quotient[quotpos] = '\0';
    printf("%s\n", reminder);
    printf("%s\n", quotient);
}