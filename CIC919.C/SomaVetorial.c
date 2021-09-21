#include <stdio.h>
#include <stdlib.h>

void contArq(FILE *f, char* arq, int *countN);
void preenche(FILE *f, char* arq, int *v);
int Somax2(int *v, int n);
int Somax3(int *v, int e, int d);
int Somax4(int *v, int n);

int main(void) 
{
  FILE *f;
  char* arq = "1M.dat"; //<-- insira o nome do arquivo aqui
  int countN = 0;
  contArq(f, arq, &countN);
  int *v = malloc(countN * sizeof(int)); if (v == NULL) return -1;
  preenche(f, arq, v);

  int max = Somax2(v, countN);
  int max2 = Somax3(v, 0, countN -1);
  int max3 = Somax4(v, countN);
  printf("%d\n%d\n%d", max, max2, max3);
  
  free(v);
  return 0;
}

void contArq(FILE *f, char* arq, int *countN)
{
  char c;
  f = fopen(arq, "r");
  if (f == NULL)
    {
        printf("Não há arquivo");
    }
    for (c = getc(f); c != EOF; c = getc(f))
        if (c == '\n')
            *countN = *countN + 1;
    fclose(f);
}

void preenche(FILE *f, char* arq, int *v)
{
  f = fopen(arq, "r");
  int i = 0;

  fscanf (f, "%d", &v[i++]);    
  while (!feof (f))
  {  
    fscanf (f, "%d", &v[i++]);      
  }
  fclose (f);
}

int Somax2(int *v, int n)
{ 
 int max = 0, aux;
 for (int i = 0; i < n; i++)
 { 
  aux = 0;
  for (int j = i; j < n; j++)
  {
    aux = aux + v[j];
    if (aux > max) 
      max = aux;
  }
 }
 return max;
}

int Somax3(int *v, int e, int d)
{
  int Elim = 0, Dlim = 0, auxE = 0, auxD = 0, max = 0;
  int Lim = (e + d) / 2;
  if(e == d)
  { 
      if(v[e] > d) return v[e];
      else return 0;
  }
  int esq = Somax3(v, e, Lim);
  int dir = Somax3(v, Lim + 1, d);

  for(int i = Lim; i >= e; i--)
  {
    auxE = auxE + v[i];
    if(auxE > Elim) Elim = auxE; 
  }
  for(int i = Lim + 1; i <= d; i++)
  {
    auxD = auxD + v[i];
    if(auxD > Dlim) Dlim = auxD; 
  }
  int soma = Elim + Dlim;
  if(esq > dir && esq > soma) max = esq;
  if(dir > esq && dir > soma) max = dir;
  if(soma > esq && soma > dir) max = soma;

  return max;
  }

  int Somax4(int *v, int n)
  {
    int max = 0, aux = 0, j = 0, k = 0;
    int ini = 0, fim = n;

    for(int i = 0; i < n; i++)
    {
      aux = aux + v[i];
      k = k + 1;
      if(aux > max)
      {
        max = aux;
        fim = k;
      }else if(aux < max)
      {
        aux = 0;
        j = k = ++i;
        ini = j;
      }
    }
    return max;
  }