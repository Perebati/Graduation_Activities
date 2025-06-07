#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct aluno{
    char nome[100];
    char curso[4];
    int matricula;
} Aluno;

Aluno leVetor(const char *charAux);
char *SepararTokens(const char *const charAux, char *buffer, size_t bufferTam);
int ObterNumeroElementos(char arquivo[]);

int main(void)
{
  char arquivo[20];
  scanf("%s", arquivo);
  char charAux[100];
  int i = 0;
  FILE  *pontoArq;
  int l = ObterNumeroElementos(arquivo);
  Aluno *v = malloc( l * sizeof(Aluno));

  pontoArq = fopen(arquivo, "r");
  if (pontoArq == NULL)
      return -1;

  while (fgets(charAux, sizeof(charAux), pontoArq) != NULL)
    {
      size_t comprimento;

      comprimento = strlen(charAux);
      if (charAux[comprimento - 1] == '\n')
          charAux[comprimento - 1] = '\0';
      v[i++] = leVetor(charAux);
    }
  fclose(pontoArq);




  //while (--i >= 0)
  //  printf("%s: %s, %i\n", v[i].nome, v[i].curso, v[i].matricula);
  //printf("%i ", ObterNumeroElementos());


  free(v);
  return 0;
}

int ObterNumeroElementos(char arquivo[])
{
    FILE *pontArq;
    char c, letra = '\n';
    int vezes = 0;
    pontArq = fopen(arquivo,"r");

    while(fread (&c, sizeof(char), 1, pontArq))
    {
        if(c == letra)
        {
            vezes++;
        }
    }
    fclose(pontArq);
    return vezes + 1;
}

char *SepararTokens(const char *const charAux, char *buffer, size_t bufferTam)
{
  char  *ponter;
  size_t comprimento;

  if ((charAux == NULL) || (buffer == NULL))
      return NULL;

  ponter = strpbrk(charAux, "\t");

  if (ponter == NULL)
      comprimento = strlen(charAux);
  else
      comprimento = ponter - charAux;

  if (comprimento >= bufferTam)
      comprimento = bufferTam - 1;

  buffer[comprimento] = '\0';
  memcpy(buffer, charAux, comprimento);

  return ponter + 1;
}

Aluno leVetor(const char *charAux)
{
  Aluno Aluno;

  charAux = SepararTokens(charAux, Aluno.nome, sizeof(Aluno.nome));
  charAux = SepararTokens(charAux, Aluno.curso, sizeof(Aluno.curso));
  Aluno.matricula = atoi(charAux);

  return Aluno;
}
