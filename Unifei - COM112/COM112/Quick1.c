//Cabeçalho
//Nome: Lucas Batista Pereira
//Matricula: 2020007290
//Algoritimos e estruturas de dados 2
//Prof. Luiz Olmes
//Exercicio 1

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct aluno{
    char nome[100];
    char curso[4];
    int matricula;
} Aluno;

//Função para obter o numero de linhas, ou seja, a quantidade de alunos.
int ObterNumeroElementos(const char arquivo[]);

//Função que recebe os tokens de "SepararTokens" e escreve num vetor de estruturas os dados.
//Retorna a estrutua pronta no vetor "v".
Aluno leVetor(const char *charAux);

//Função para subdividir uma linha auxiliar de um subvetor
char *SepararTokens(const char *const charAux, char *buffer, size_t bufferTam);

//Parecido com partição comum, a maior diferença sendo que esta compara
//strings com a função "strcmp" de "string.h".
int particao(Aluno *v, int p, int r);
void quicksort(Aluno *v, int p, int r);

int main(void)
{
  char arquivo[40];
  scanf("%s", arquivo);
  char charAux[100]; //Criação da linha auxiliar
  int i = 0;
  FILE  *pontoArq;
  int l = ObterNumeroElementos(arquivo);
  Aluno *v = malloc( l * sizeof(Aluno)); //Alocação do vetor de estruturas a partir da quantidade de linhas.

  pontoArq = fopen(arquivo, "r");
  if (pontoArq == NULL)
      return -1;

  while (fgets(charAux, sizeof(charAux), pontoArq) != NULL) //Lê linha por linha do arquivo
  {
    size_t comprimento;

    comprimento = strlen(charAux); //Defini o limite de CharAux
    if (charAux[comprimento - 1] == '\n') //Substituição de "Espaço" por "final da string"
        charAux[comprimento - 1] = '\0';
    v[i++] = leVetor(charAux);
  }
  fclose(pontoArq);

  quicksort(v, 0, l - 1);
  for(int i = 1; i < l; i++)
  {
  printf("%s %s %i\n", v[i].nome, v[i].curso, v[i].matricula);
  }

  free(v);
  return 0;
}

int ObterNumeroElementos(const char arquivo[])
{
    //Checa quantas vezes "\n" está presente, com isso a função
    //retorna um 'int' que representa o número de alunos.
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

Aluno leVetor(const char *charAux)
{
  Aluno Aluno;

  charAux = SepararTokens(charAux, Aluno.nome, sizeof(Aluno.nome));
  charAux = SepararTokens(charAux, Aluno.curso, sizeof(Aluno.curso));
  Aluno.matricula = atoi(charAux);

  return Aluno;
}

char *SepararTokens(const char *const charAux, char *buffer, size_t bufferTam)
{
  //Manipula diretamente 'charAux', que sempre receberá novos dados até o final do arquivo.
  //Buffer é utilizado para subdividir a linha em 'tokens'
  //bufferTam é utilizado como parametro das subdivisões
  char  *ponter;
  size_t comprimento;

  if ((charAux == NULL) || (buffer == NULL))
      return NULL;

  ponter = strpbrk(charAux, "\t");

  //Ponter vai receber a posição do 'tab'. Caso ele não receba, siginifica que está
  // no final da linha auxiliar.
  if (ponter == NULL)
      comprimento = strlen(charAux);
  else
      comprimento = ponter - charAux;

  if (comprimento >= bufferTam)
      comprimento = bufferTam - 1;

  buffer[comprimento] = '\0';
  memcpy(buffer, charAux, comprimento);

  return ponter + 1; //Retorna a posição do endereço do 'token'
}

int particao(Aluno *v, int p, int r)
{
  int i = p, j = r + 1;
  char *piv;
  piv = v[p].nome;

  Aluno aux;

  while(1)
  {
    while(strcmp(v[++i].nome,piv) < 0) if(i == r) break;
    while(strcmp(v[--j].nome,piv) > 0 ) if(j == p) break;


    if(i >= j) break;

    aux = v[i];
    v[i] = v[j];
    v[j] = aux;
  }
  aux = v[p];
  v[p] = v[j];
  v[j] = aux;

  return j;
}

void quicksort(Aluno *v, int p, int r)
{
  int q;

  if(p < r)
  {
    q = particao(v, p, r);
    quicksort(v, p, q - 1);
    quicksort(v, q + 1, r);
  }
}





