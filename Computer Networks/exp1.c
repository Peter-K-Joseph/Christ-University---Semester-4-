#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    char string[20], flag, stuffed, buffer, stuffed_string[40], destuffed_string[20];
    int i = 0, j = 1;
    printf("Enter the string: ");
    fgets(string, 20, stdin);
    string[strlen(string) - 1] = '\0';
    printf("Enter the flag: ");
    scanf("%c", &flag);
    printf("Enter the string: ");
    scanf("%c", &buffer);
    scanf("%c", &stuffed);
    stuffed_string[0] = flag;
    for (int i = 0; i < strlen(string); i++)
    {
        if (string[i] == flag || string[i] == stuffed)
        {
            stuffed_string[j] = stuffed;
            j = j + 1;
        }
        stuffed_string[j] = string[i];
        j += 1;
        if (i > 20)
        {
            printf("[ERROR] BUFFER OVERFLOW\n");
            break;
        }
    }
    stuffed_string[j] = flag;
    stuffed_string[j+1] = '\0';
    printf("Stuffed String: %s\n", stuffed_string);
    j = 0;
    for (int i = 1; i < strlen(stuffed_string) - 1; i++, j++)
    {
        if (stuffed_string[i] == stuffed)
            i++;
        destuffed_string[j] = stuffed_string[i];
    }
    destuffed_string[j] = '\0';
    printf("Destuffed String: %s\n", destuffed_string);
}