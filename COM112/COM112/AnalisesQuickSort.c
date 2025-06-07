#include <stdio.h>
#include <stdlib.h>

void quicksortHoare(int *v, int p, int r, int *c1, int *t1);
int particaoHoare(int *v, int p, int r, int *c1, int *t1);
void quicksortLomuto(int *v, int p, int r, int *c2, int *t2);
int particaoLomuto(int *v, int p, int r, int *c2, int *t2);
void quicksortSedge(int *v, int p, int r, int *c3, int *t3);
int particaoSedge(int *v, int p, int r, int *c3, int *t3);
void leVetor(int *v1, int *v2, int *v3, int n);
void imprimir(int *v1, int *v2, int *v3, int n);
void imprimirCT(int c1, int c2, int c3, int t1, int t2, int t3);


int main(void)
{
int n;
int c1 = 0, t1 = 0;
int c2 = 0, t2 = 0;
int c3 = 0, t3 = 0;

scanf("%i", &n);

int *v1 = malloc( n * sizeof(int)); if(v1 == NULL) return -4;
int *v2 = malloc( n * sizeof(int)); if(v2 == NULL) return -5;
int *v3 = malloc( n * sizeof(int)); if(v3 == NULL) return -6;

leVetor(v1, v2, v3, n);

quicksortHoare(v2, 0, n - 1, &c1, &t1);
quicksortLomuto(v1, 0, n - 1, &c2, &t2);
quicksortSedge(v3, 0, n - 1, &c3, &t3);

//imprimir(v1, v2, v3, n);
imprimirCT(c1, c2, c3, t1, t2, t3);

free(v1);
free(v2);
free(v3);
return 0;
}

void imprimirCT(int c1, int c2, int c3, int t1, int t2, int t3)
{
  printf("%i %i\n", c1, t1);
  printf("%i %i\n", c2, t2);
  printf("%i %i\n", c3, t3);
}
void imprimir(int *v1, int *v2, int *v3, int n)
{
for(int i = 0; i < n; i++)
{
  printf("%i ", v1[i]);
}
printf("\n");
for(int i= 0; i < n; i++)
{
  printf("%i ", v2[i]);
}
printf("\n");
for(int i= 0; i < n; i++)
{
  printf("%i ", v3[i]);
}
}
void leVetor(int *v1, int *v2, int *v3, int n)
{
  for(int i = 0; i < n; i++)
  {
  scanf("%d", &v1[i]);
  v3[i] = v2[i] = v1[i];
  }
}

void quicksortHoare(int *v, int p, int r, int *c1, int *t1)
{
  int q;
  if(p < r)
  {
    q = particaoHoare(v, p, r, c1, t1);
    quicksortHoare(v, p, q, c1, t1);
    quicksortHoare(v, q + 1, r, c1, t1);
  }
}
/*"Olhando aqui a sua função, temos que lembrar que no livro do Cormen, a primeira posição do vetor é 1, e não 0. Nesse caso, quando o vetor começa em 0, na função quicksortHoare, a primeira invocação recursiva passa o limite do vetor como q, ao invés de q-1."*/
int particaoHoare(int *v, int p, int r, int *c1, int *t1)
{
  int piv = v[p], i = p - 1, j = r + 1, aux;

      while (1)
      {
        do
        {
          j--;
          (*c1)++;
        }while (v[j] > piv);

        do
        {
          i++;
          (*c1)++;
        }while (v[i] < piv);

        if(i >= j)
        {
          return j;
        }

        (*t1)++;
        aux = v[i];
        v[i] = v[j];
        v[j] = aux;
      }

}


void quicksortLomuto(int *v, int p, int r, int *c2, int *t2)
{
  int q;
  if(p < r)
  {
    q = particaoLomuto(v, p, r, c2, t2);
    quicksortLomuto(v, p, q - 1, c2, t2);
    quicksortLomuto(v, q + 1, r, c2, t2);
  }
}

int particaoLomuto(int *v, int p, int r, int *c2, int *t2)
{
  int piv = v[r];
  int i = p, aux, j;

  for(j = p; j < r; j++)
  {
    (*c2)++;
    if(v[j] < piv)
    {
      (*t2)++;
      aux = v[i];
      v[i] = v[j];
      v[j] = aux;
      i++;
    }
  }
  (*t2)++;
  aux = v[i];
  v[i] = v[j];
  v[j] = aux;

  return i;
}

void quicksortSedge(int *v, int p, int r, int *c3, int *t3)
{
  int q;
  if(p < r)
  {
    q = particaoSedge(v, p, r, c3, t3);
    quicksortSedge(v, p, q - 1, c3, t3);
    quicksortSedge(v, q + 1, r, c3, t3);
  }
}

int particaoSedge(int *v, int p, int r, int *c3, int *t3)
{
  int i = p, j = r + 1, piv = v[p], aux;

  while(1)
  {
    while(v[++i] < piv)
    {
      if(i == r) break;
    }
    while(piv < v[--j])
    {
      if(j == p) break;
    }
    if (i >= j)
    {
      break;
    }
    (*t3)++;
    aux = v[i];
    v[i] = v[j];
    v[j] = aux;
  }
  (*t3)++;
  aux = v[p];
  v[p] = v[j];
  v[j] = aux;

  (*c3) = (*c3) + (i - p) + ((r + 1) - j);

  return j;
}
