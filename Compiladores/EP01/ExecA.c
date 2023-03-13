#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int compilador(char cadeia[]);
char check_op(char op);
char check_char(char c);
char check_num(char letra);

int main(void)
{

  char cadeia[255] = "i(2+4>1)2+5e6k1";

  compilador(cadeia);
}

char check_num(char letra)
{

  if (letra == '0' || letra == '1' || letra == '2' || letra == '3' || letra == '4' || letra == '5' || letra == '6' || letra == '7' || letra == '8' || letra == '9')
  {

    if (letra == '3' || letra == '1' || letra == '2')
    {
      return 'S';
    }

    if (letra == '6' || letra == '5' || letra == '4')
    {
      return 'S';
    }
  }

  return 'F';
}

char check_op(char op)
{

  if (op == '(' || op == ')' || op == '>' || op == '=' || op == '-' || op == '+')
  {

    return op;
  }

  return '0';
}

char check_char(char c)
{

  if (c == 'i' || c == 'e' || c == 'w' || c == 'x')
  {
    return toupper(c);
  }

  return '0';
}

int compilador(char cadeia[])
{

  int tamanho_cadeia = strlen(cadeia);
  int i = 0;

  while (i < tamanho_cadeia)
  {

    if (check_char(cadeia[i]) != '0')
    {
      printf("simbol --> %c | token --> %c\n", cadeia[i], check_char(cadeia[i]));
    }

    if (check_num(cadeia[i]) != 'F')
    {
      printf("simbol --> %c | token --> %c\n", cadeia[i], check_num(cadeia[i]));
    }

    char op = check_op(cadeia[i]);

    if (op != '0')
    {

      if (op == '(')
      {
        printf("simbol --> %c | token --> ABR\n", op);
      }

      else if (op == ')')
      {
        printf("simbol --> %c | token --> FECH\n", op);
      }

      else if (op == '>')
      {
        printf("simbol --> %c | token --> MAIOR\n", op);
      }

      else if (op == '=')
      {
        printf("simbol --> %c | token --> ATRIB\n", op);
      }

      else if (op == '-')
      {
        printf("simbol --> %c | token --> SUB\n", op);
      }

      else if (op == '+')
      {
        printf("simbol --> %c | token --> SOM\n", op);
      }
      
    }
    i++;
  }
}