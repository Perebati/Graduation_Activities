#include <stdio.h>
#include <stdlib.h>

void mergeSort(int *v, int p, int r);
void intercala(int *v, int p, int q, int r);
void leVetor(int *v,  unsigned int n);

int c;
int t;

int main(void)
{
    unsigned int n;

	scanf("%u", &n);

	int *v = NULL;
	v = malloc(n * sizeof(int) );
	if(v == NULL) exit(1);

	leVetor(v, n);
	mergeSort(v, 0, n);

    //for(int i = 0; i < n; i++)
    //{ printf("%d ", v[i]);
    //}
	printf("%u %u", c, t);

	free(v);

	return 0;
}

void mergeSort(int *v, int p, int r)
{
    if(p < r - 1)
    {
        int q = (p +  r) / 2;

        mergeSort(v, p, q);
        mergeSort(v, q, r);
        intercala(v, p, q, r);
    }
}

void intercala(int *v, int p, int q, int r)
{
    int i, j, k;
    int *w;

    w = malloc((r - p) * sizeof(int));
    i = p;
    j = q;
    k = 0;


    while( i < q && j < r)
    {
        c++;
        if(v[i] <= v[j])
        {
            t++;
            w[k] = v[i];
            k++;
            i++;

        }
        else
        {
            t++;
            w[k] = v[j];
            k++;
            j++;
        }
    }

    while(i < q)
    {
        t++;
        w[k] = v[i];
        k++;
        i++;
    }
    while( j < r)
    {
        t++;
        w[k] = v[j];
        k++;
        j++;
    }

    for(i = p; i < r; i++)
    {
        t++;
        v[i] = w[i - p];
    }
    free(w);
}

void leVetor(int *v,  unsigned int n)
{
	for(int i = 0; i < n; i++)
		scanf("%i", &v[i]);
}


