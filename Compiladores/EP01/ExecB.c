#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int checaCadeia(char cadeia[], int len);

int main(void)
{

    char binario[5] = "0100";

    int len = strlen(binario);

    checaCadeia(binario, len);

    return 0;
}

int checaCadeia(char cadeia[], int len)
{

    if (len > 5)
    {
        printf("NMULT, %s\n", cadeia);
        return -1;
    }

    int s = 0, i = 0, falhou = 0;

    while (i < len)
    {

        char c = cadeia[i];

        switch (s)
        {
        case (0):
            if (c == '1')
            {
                s = 1;
                break;
            }
            else
            {
                falhou = 1;
                break;
            }

        case (1):
            if (c == '1')
            {
                s = 2;
                break;
            }
            else
            {
                falhou = 1;
                break;
            }

        case (2):
            if (c == '0')
            {
                s = 3;
                break;
            }
            else
            {
                falhou = 1;
                break;
            }

        case (3):
            if (c == '0')
            {
                s = 4;
                break;
            }
            else
            {
                falhou = 1;
                break;
            }
        }

        if (falhou == 1)
        {
            break;
        }
        else
        {
            i++;
        }
    }

    if (s == 3 || s == 4)
    {
        printf("MULT, %s\n", cadeia);
    }
    else
    {
        printf("NMULT, %s\n", cadeia);
    }
}
