#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char input[50], reciever_side[50], quot[50], rem[4], key[4];

void checkSumXOR(int mode)
{
    int i, j;
    char temp[4], key_duplicate[4], data[50];
    (mode == 1)? strcpy(data, input): strcpy(data, reciever_side);
    int len_key = strlen(key);
    int len_msg = strlen(data);
    strcpy(key_duplicate, key);
    for (i = 0; i < len_key - 1; i++)
    {
        data[len_msg + i] = '0';
    }
    for (i = 0; i < len_key; i++)
    {
        temp[i] = data[i];
    }
    for (i = 0; i < len_msg; i++)
    {
        quot[i] = temp[0];
        if (quot[i] == '0')
        {
            for (j = 0; j < len_key; j++)
                key[j] = '0';
        }
        else
        {
    for (j = 0; j < len_key; j++)
                key[j] = key_duplicate[j];
        }
        for (j = len_key - 1; j > 0; j--)
            rem[j - 1] = (temp[j] == key[j]) ? '0' : '1';
        rem[len_key - 1] = data[i + len_key];
        strcpy(temp, rem);
    }
    strcpy(rem, temp);
    if (mode == 1) {
		input[0] = '\0';
		strcpy(input, data);
	} else {
		reciever_side[0] = '\0';
		strcpy(reciever_side, data);
	}
}

int main()
{
    // DRIVER CODE
    char temp[4], key_duplicate[4], buffer;
    int i, j, len_key, len_msg, flag = 0, ch_index;

    // SENDER SIDE
    printf("Enter the key: ");
    scanf("%s", key);
    len_key = strlen(key);
    printf("Enter the message: ");
    scanf("%c", input);
    fgets(input, 50, stdin);
    input[strlen(input) - 1] = '\0';
    len_msg = strlen(input);
    checkSumXOR(1);
    printf("The Quotient is: %s\n", quot);
    printf("The Remainder is: %s\n", rem);
    for (i = 0; i < len_msg; i++)
    {
        reciever_side[i] = input[i];
    }
    for (i = 0; i < len_key - 1; i++, j++)
        reciever_side[len_msg + i] = rem[i];
    reciever_side[len_msg + len_key] = '\0';
    printf("The Final Data sent: %s\n", reciever_side);
    printf("\n");
    
    printf("Enter location to be modified (enter -1 to skip): ");
	scanf("%i", &ch_index);
	if (ch_index > strlen(reciever_side) || ch_index < 0) {
		printf("Skipping Data modification. Array out of bounds\n");
	} else {
		if (reciever_side[ch_index] == '0')
			reciever_side[ch_index] = '1';
		else
			reciever_side[ch_index] = '0';
	}
	checkSumXOR(0);
	for (i = 0; i < strlen(rem); i++) {
		if (rem[i] == '1') {
			flag = 1;
			break;
		}
	}
	(flag == 1)? printf("Transmission Error Detected"): printf("Transmission Successful");
}
