#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int checaCadeia(char cadeia[]);
int verificaVogal(char letra);
int verificaSeEhLetra(char letra);

int main(void)
{

    char cadeia[3] = "a2e";
    checaCadeia(cadeia);

    return 0;
}

int verificaVogal(char letra)
{

    if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u' ||
        letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U')
    {
        return 1;
    }

    return 0;
}


int checaCadeia(char cadeia[])
{

    int len = strlen(cadeia);

    if (len != 3)
    {
        printf("NPAL, %s\n", cadeia);
        return -1;
    }

    int s = 0, i = 0, falhou = 0;

    while (i < len)
    {

        char c = cadeia[i];

        switch (s)
        {

        case (0):

            if (verificaVogal(c) == 1)
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
            if (verificaSeEhLetra(c) == 1)
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
            if (verificaVogal(c) == 1)
            {
                s = 3;
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

    if (s == 3)
    {
        printf("PAL, %s\n", cadeia);
    }
    else
    {
        printf("NPAL, %s\n", cadeia);
    }
}


int verificaSeEhLetra(char letra)
{

    if (isalpha(letra))
    {
        return 1;
    }

    return 0;
}