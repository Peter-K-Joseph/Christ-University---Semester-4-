#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int stack = 0, j = 0;
    char data[20], stuffed_data[40], destuffed_data[20];
    printf("Enter the string: ");
    fgets(data, 20, stdin);
    data[strlen(data) - 1] = '\0';
    for (int i = 0 ; i < strlen(data); i++, j++) {
        stack = (data[i] == '1')? stack+1: 0;
        if (stack == 6) {
            stuffed_data[j] = '0';
            stack = 0;
            j++;
        }
        stuffed_data[j] = data[i]; 
    }
    stuffed_data[j] = '\0';
    printf("Stuffed Data: %s\n", stuffed_data);
    j = stack = 0;
    for (int i = 0 ; i < strlen(stuffed_data); i++, j++) {
        stack = (data[i] == '1')? stack+1: 0;
        if (stack == 6) i++;
        destuffed_data[j] = data[i];
    }
    destuffed_data[j] = '\0';
    printf("Destuffed Data: %s", destuffed_data);
}