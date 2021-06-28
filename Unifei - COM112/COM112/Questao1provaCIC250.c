//CIC 250
//Nome: Lucas Batista Pereira
//Matr�cula: 2020007290
//Posi��o falsa EP01.3

#include <stdio.h>
#include <math.h>

double func(double x); //<--Fun��es para fun��es
double derivada(double x);

int main(void)
{

    double e, x, x0, x1; //<--Vari�veis essenciais.
    int k, i = 0; //<-- Contadores

    scanf("%lf %d %lf", &x0, &k, &e);

    if(fabs(func(x0)) < e)  //<--Check-up de condi��es.
    {
        x = x0;
        return 0;
    }

    x1 = x0 - (func(x0)/derivada(x0));


    while(i < k) //<--Check-up de condi��es.
    {
      x0 = x1;
      i++;
      x1 = x0 - (func(x0)/derivada(x0));

        if(fabs(func(x0)) < e) //<--Check-up de condi��es. Se verdade, encerra while.
        {
        x = x0;
        break;
        }
    }
    x = x1;


    printf("%lf\n%lf\n%d", x, func(x), i);
    return 0;
}


double func(double x)
{
  double y = 4 * x - pow(2.718281828459045235360287, x);
  return y;
}

double derivada(double x)
{
  double y = 4 - pow(2.718281828459045235360287, x);
  return y;
}

