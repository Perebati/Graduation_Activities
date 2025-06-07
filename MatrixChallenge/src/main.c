#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Color{
    int r, g, b;
} Color;

typedef struct Mask{
    int m1, m2, m3;
} Mask;

Color** alocarMatrizColor(int n) {
    Color** matriz = (Color**)malloc(n * sizeof(Color*));
    for (int i = 0; i < n; i++) {
        matriz[i] = (Color*)malloc(n * sizeof(Color));
    }
    return matriz;
}

Mask** alocarMatrizMask(int n) {
    Mask** matriz = (Mask**)malloc(n * sizeof(Mask*));
    for (int i = 0; i < n; i++) {
        matriz[i] = (Mask*)malloc(n * sizeof(Mask));
    }
    return matriz;
}

void liberarMatrizColor(Color** matriz, int n) {
    for (int i = 0; i < n; i++) {
        free(matriz[i]);
    }
    free(matriz);
}


void liberarMatrizMask(Mask** matriz, int n) {
    for (int i = 0; i < n; i++) {
        free(matriz[i]);
    }
    free(matriz);
}

Color** multiplicarMatrizes(Color** matrizColor, Mask** matrizMask, int n) {
    Color** resultado = alocarMatrizColor(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            resultado[i][j].r = 0;
            resultado[i][j].g = 0;
            resultado[i][j].b = 0;

            for(int k = 0; k < n; k++){
                resultado[i][j].r += matrizColor[i][k].r * matrizMask[k][j].m1;
                resultado[i][j].g += matrizColor[i][k].g * matrizMask[k][j].m2;
                resultado[i][j].b += matrizColor[i][k].b * matrizMask[k][j].m3;
            }
      
        }
    }
    return resultado;
}

int main() {
    char codification[3];
    unsigned int i, j, k, n1, n2, max_color_scale, r, g, b, m1, m2, m3;
    
    scanf("%2s", codification);

    if (strcmp(codification, "P3") != 0 && strlen(codification) != 2) {
        printf("Erro: Código inválido. Deve ser \"P3\"!\n");
        return 1;
    }

    scanf("%u %u", &n1, &n2);

    if(n1 != n2){
        printf("Erro: Os valores para \"n\" devem ser inteiro positvos iguais!\n");
    }

    scanf("%u", &max_color_scale);

    Color** matrizColor = alocarMatrizColor(n1);
    Mask** matrizMask = alocarMatrizMask(n1);

    for (i = 0; i < n1; i++) {
        for (j = 0; j < n1; j++) {
            scanf("%d %d %d", &r, &g, &b);

            if (r > max_color_scale || g > max_color_scale || b > max_color_scale) {
                printf("Valor de cor inválido. Deve ser menor ou igual a %u.\n", max_color_scale);
                return 1;
            }

            matrizColor[i][j].r = r;
            matrizColor[i][j].g = g;
            matrizColor[i][j].b = b;
        }
    }

    for (i = 0; i < n1; i++) {
        for (j = 0; j < n1; j++) {
            scanf("%d %d %d", &m1, &m2, &m3);

            if ((m1 != 0 && m1 != 1) || (m2 != 0 && m2 != 1) || (m3 != 0 && m3 != 1)) {
                printf("Valores inválidos. m1, m2 e m3 devem ser 0 ou 1.\n");
                return 1;
            }

            matrizMask[i][j].m1 = m1;
            matrizMask[i][j].m2 = m2;
            matrizMask[i][j].m3 = m3;
        }
    }

    Color** resultado = multiplicarMatrizes(matrizColor, matrizMask, n1);

    printf("%s\n", codification);
    printf("%d %d\n", n1, n2);
    printf("%d\n", max_color_scale);

    for (i = 0; i < n1; i++) {
        for (j = 0; j < n1; j++) {
            printf("%d %d %d ", resultado[i][j].r, resultado[i][j].g, resultado[i][j].b);
        }
        printf("\n");
    }

    liberarMatrizColor(matrizColor, n1);
    liberarMatrizMask(matrizMask, n1);
    liberarMatrizColor(resultado, n1);

    return 0;
}
