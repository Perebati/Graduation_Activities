// Exercicio referente a criação de uma rede neural para disciplina CIC260.1
// Grupo:   		JOÃO PEDRO MALTA ARDO - 2020029126
//			      LUCAS BATISTA PEREIRA - 2020007290
//             MARCELO ROBERT SANTOS - 2020002777
// Nessa rede Neural, o intuito é calcular a probabilidade de chuva referente a umidade do ar
// Para treinamento, há 15 dados de entrada.

// Após o treinamento, basta digitar um valor referente a porcetagem do ar para o programa dizer a
// probalidade de chuva

// Obs: Há um certo delay na impressão do porcentagem de chuva no console, por isso,
//é necessario digitar a mesma entrada DUAS vezes.

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define InputN 1
#define HN 2
#define OutN 1
#define datanum 15
int main()
{
    double sigmoid(double);
    char buffer[200];
    double x_out[InputN];
    double hn_out[HN];
    double y_out[OutN];
    double y[OutN];
    double w[InputN][HN];
    double v[HN][OutN];

    double deltaw[InputN][HN];
    double deltav[HN][OutN];

    double hn_delta[HN];
    double y_delta[OutN];
    double error;
    double errlimit = 0.01;
    double alpha = 0.1, beta = 0.1;
    int loop = 0;
    int times = 100;
    int i, j, m;
    double max, min;
    double sumtemp;
    double errtemp;

    struct
    {
        double input[InputN];
        double teach[OutN];
    } data[datanum];

    data[0].input[0] = 51;
    data[0].teach[0] = -1;

    data[1].input[0] = 53;
    data[1].teach[0] = -1;

    data[2].input[0] = 86;
    data[2].teach[0] = 1;

    data[3].input[0] = 84;
    data[3].teach[0] = 1;

    data[4].input[0] = 82;
    data[4].teach[0] = -1;

    data[5].input[0] = 49;
    data[5].teach[0] = -1;

    data[6].input[0] = 38;
    data[6].teach[0] = -1;

    data[7].input[0] = 83;
    data[7].teach[0] = 1;

    data[8].input[0] = 82;
    data[8].teach[0] = 1;

    data[9].input[0] = 86;
    data[9].teach[0] = -1;

    data[10].input[0] = 58;
    data[10].teach[0] = 1;

    data[11].input[0] = 79;
    data[11].teach[0] = -1;

    data[12].input[0] = 62;
    data[12].teach[0] = 1;

    data[13].input[0] = 93;
    data[13].teach[0] = 1;

    data[14].input[0] = 62;
    data[14].teach[0] = 1;

    // Inicializa a entrada e saída esperada
    for (m = 0; m < datanum; m++)
    {
        for (i = 0; i < InputN; i++)
            data[m].input[i] = data[m].input[i] / 100;
    }
    // Inicia os pesos
    // Da camada de entrada até a intermediária
    for (i = 0; i < InputN; i++)
    {
        for (j = 0; j < HN; j++)
        {
            w[i][j] = 0.5;
            deltaw[i][j] = 0;
        }
    }

    // Da camada intermediária até a de saída
    for (i = 0; i < HN; i++)
    {
        for (j = 0; j < OutN; j++)
        {
            v[i][j] = 0.5;
            deltav[i][j] = 0;
        }
    }

    // Training
    while (loop < times)
    {
        loop++;
        error = 0.0;

        for (m = 0; m < datanum; m++)
        {
            // Feedforward
            max = 0.0;
            min = 0.0;
            for (i = 0; i < InputN; i++)
            {
                x_out[i] = data[m].input[i];
            }

            for (i = 0; i < OutN; i++)
            {
                y[i] = data[m].teach[i];
            }

            for (i = 0; i < HN; i++)
            {
                sumtemp = 0.0;
                for (j = 0; j < InputN; j++)
                    sumtemp += w[j][i] * x_out[j];
                hn_out[i] = sigmoid(sumtemp);
            }
            // hn_out são os dados da camada intermediária, isto é, entradas x[i] *  pesos w[i]

            for (i = 0; i < OutN; i++)
            {
                sumtemp = 0.0;
                for (j = 0; j < HN; j++)
                    sumtemp += v[j][i] * hn_out[j];
                y_out[i] = sigmoid(sumtemp);
            }
            // y_out são os dados da camada de saída, isto é, dados da camada intermediária hn_out[i] * pesos v[i]

            // Backpropagation
            for (i = 0; i < OutN; i++)
            {
                errtemp = y[i] - y_out[i];
                y_delta[i] = -errtemp * sigmoid(y_out[i]) * (1.0 - sigmoid(y_out[i]));
                error += errtemp * errtemp;
            }

            for (i = 0; i < HN; i++)
            {
                errtemp = 0.0;
                for (j = 0; j < OutN; j++)
                    errtemp += y_delta[j] * v[i][j];
                hn_delta[i] = errtemp * (1.0 + hn_out[i]) * (1.0 - hn_out[i]);
            }

            // Stochastic gradient descent
            for (i = 0; i < OutN; i++)
            {
                for (j = 0; j < HN; j++)
                {
                    deltav[j][i] = alpha * deltav[j][i] + beta * y_delta[i] * hn_out[j];
                    v[j][i] -= deltav[j][i];
                }
            }

            for (i = 0; i < HN; i++)
            {
                for (j = 0; j < InputN; j++)
                {
                    deltaw[j][i] = alpha * deltaw[j][i] + beta * hn_delta[i] * x_out[j];
                    w[j][i] -= deltaw[j][i];
                }
            }
        }

        // Global error
        error = error / 2;
        if (loop % 1000 == 0)
        {
            // printf("Global Error = %f\n", error);
        }
        if (error < errlimit)
            break;
        // printf("The %d th training, error: %f\n", loop, error);
    }

    double testeEntrada[InputN];
    printf("w = %f v = %f\n", w[0][0], v[0][0]);
    while (1)
    {
        for (i = 0; i < InputN; i++)
        {
            printf("Digite a umidade a ser observada: ");
            scanf(" %lf\n ", &testeEntrada[i]);
        }
        // Realiza o cálculo da saída utilizando os pesos obtidos
        // Passa para a camada intermediária
        for (i = 0; i < HN; i++)
        {
            for (j = 0; j < InputN; j++)
                sumtemp = w[j][i] * testeEntrada[j];
            hn_out[i] = sigmoid(sumtemp);
        }
        // Passa para a camada de saída e já imprime cada resultado
        for (i = 0; i < OutN; i++)
        {
            for (j = 0; j < HN; j++)
                sumtemp = v[j][i] * hn_out[j];
            y_out[i] = sigmoid(sumtemp);
            if (y_out[i] > 0.3)
                printf("y%d = %.2f% \n", i, (1.8 * y_out[i]));
            else
                printf("y%d = %.2f% \n", i, (0.8 * y_out[i]));
        }
    }

    return 0;
}

// sigmoid serves as avtivation function
double sigmoid(double x) { return (1.0 / (1.0 + exp(-x))); }