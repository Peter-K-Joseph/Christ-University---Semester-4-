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
    char string[100], key[4], key_duplicate[4], temp[10], quotient[50], reminder[5], buffer;
    int err_pos, quotpos = 0, length_key, length_msg;
    printf("Enter a string: ");
    fgets(string, 100, stdin);
    string[strlen(string) - 1] = '\0';
    printf("Enter a key: ");
    fgets(key, 4, stdin);
    key[strlen(key) - 1] = '\0';
    length_key = strlen(key);
    length_msg = strlen(string);
    if (strlen(string) < 4) {
        printf("Error: String is too short.\n");
        return 0;
    }
    strcpy(key_duplicate, key);
    for (int i = 0; i < length_key-1; i++) {
        string[length_msg+i] = '0';
    }
    for (int i = 0; i < length_key; i++) {
        temp[i] = string[i];
    }
    for (int i = 0 ; i < length_msg; i++) {
        quotient[i] = temp[0];
        if (quotient[i] == '0') {
            for (int j = 0; j < length_key; j++) {
                key[j] = '0';
            }
        } else {
            for (int j = 0; j < length_key; j++) {
                key[j] = key_duplicate[j];
            }
        }
        for (int j = length_key-1; j > 0; j--) {
            if (temp[j] == key[j]) {
                if (temp[j] == key[j]) {
                    reminder[j-1] = '0';
                } else {
                    reminder[j-1] = '1';
                }
            }
        }
        reminder[length_key-1] = string[i+length_key];
        strcpy(temp, reminder);
    }
    strcpy(reminder, temp);
    printf("Quotient: %s\nReminder: %s\nData: %s%s", quotient, reminder, string, reminder);
}