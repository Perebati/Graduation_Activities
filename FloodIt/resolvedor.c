/**************************************
Aqui voce pode mudar tudo, exceto a
assinatura da funcao "resolvedor"
pode inclusive ignorar tudo se preferir
***************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Tres registros que serao uteis, Arcos, Vertices e Digrafos
typedef struct arco
{
  int ini, fim;
  struct arco *prox;
} Arco;

typedef struct vertice
{
  int id;
  Arco *arcos_saida;
  int visitado;
  int ramo_principal;
  int cor;
} Vertice;

typedef struct digrafo
{
  int n;
  int m;
  Vertice *V;
} Digrafo;

void seta_cor(Digrafo *D, int v, int cor) { D->V[v].cor = cor; }

Digrafo *criar_grafo(int n)
{
  Digrafo *G = (Digrafo *)malloc(sizeof(Digrafo));
  G->V = (Vertice *)malloc(n * sizeof(Vertice));
  G->n = n;
  G->m = 0;
  for (int u = 0; u < n; u++)
  {
    G->V[u].id = u;
    G->V[u].arcos_saida = NULL;
    G->V[u].visitado = 0;
    if (u == 0)
      G->V[u].ramo_principal = 1;
    else
      G->V[u].ramo_principal = 0;
  }
  return G;
}

Arco *criar_arco(int ini, int fim)
{
  Arco *A = (Arco *)malloc(sizeof(Arco));
  A->ini = ini;
  A->fim = fim;
  A->prox = NULL;
  return A;
}

void adiciona_arco(Digrafo *G, int ini, int fim)
{
  G->m++;
  Arco *saida = criar_arco(ini, fim);
  saida->prox = G->V[ini].arcos_saida;
  G->V[ini].arcos_saida = saida;
  return;
}

// funcao para imprimir um digrafo no formato GraphViz
// voce pode usar uma ferramente online como o
// https://dreampuf.github.io/GraphvizOnline/ para desenha seu grafo nesse
// formato (soh para grafos pequenos)
void imprime_digrafo(Digrafo *G)
{
  char *cores[] = {"red", "orange", "purple", "yellow", "green", "cyan"};
  printf("digraph G{\n");
  for (int i = 0; i < G->n; i++)
  {
    printf("  %d[style=filled,color=%s];\n", i, cores[G->V[i].cor]);
  }
  for (int i = 0; i < G->n; i++)
  {
    // u eh o i-esimo vertice
    Vertice u = G->V[i];
    for (Arco *a = u.arcos_saida; a != NULL; a = a->prox)
    {
      printf("  %d -> %d;\n", a->ini, a->fim);
    }
  }
  printf("}\n");
}

// funcoes para liberar a memoria do digrafo
void libera_lista_arcos(Arco *lista)
{
  if (lista == NULL)
    return;
  libera_lista_arcos(lista->prox);
  free(lista);
}

void libera_digrafo(Digrafo *G)
{
  for (int i = 0; i < G->n; i++)
  {
    libera_lista_arcos(G->V[i].arcos_saida);
  }
  free(G->V);
  free(G);
}

void muda_cor(Digrafo *D, int id, int cor, int *cor_vec)
{
  // Jah esta dessa cor nada a fazer
  if (D->V[id].cor == cor)
    return;
  // printf("mudando a cor do vertice %d para %d\n", id, cor);
  // Roxo
  int cor_antiga = D->V[id].cor;
  // mudando a cor antes de propagar (pode evitar um loop infinito)
  D->V[id].cor = cor;

  for (Arco *a = D->V[id].arcos_saida; a != NULL; a = a->prox)
  {
    int vizinho = a->fim;
    if (D->V[vizinho].cor == cor_antiga)
    {
      // cor_vec[D->V[vizinho].cor] -= 1;
      muda_cor(D, vizinho, cor, cor_vec);
    }
  }
  return;
}

int verifica_fim(Digrafo *D)
{
  int cor_inicial = D->V[0].cor;
  for (int v = 1; v < D->n; v++)
  {
    if (cor_inicial != D->V[v].cor)
      return 0;
  }
  return 1;
}

// Trab01 do Hokama começa aqui---------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------

// Seta_ramo é necessário para manter em ordem os vertices do ramo
// principal--------------
void seta_ramo(Digrafo *D, int id)
{
  if (D->V[id].ramo_principal == 1)
  {
    return;
  }
  else
  {
    D->V[id].ramo_principal = 1;
  }

  int cor = D->V[id].cor;
  for (Arco *a = D->V[id].arcos_saida; a != NULL; a = a->prox)
  {
    int vizinho = a->fim;
    if (D->V[vizinho].cor == cor)
    {
      seta_ramo(D, vizinho);
    }
  }
  return;
}

void ramo_DFS(Digrafo *D, int vertex, int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    D->V[i].ramo_principal = 0;
  }
  seta_ramo(D, 0);
}
// Seta_ramo é necessário para manter em ordem os vertices do ramo
// principal--------------

// DFS-------------------------------------------------------------
void DFS(Digrafo *D, int vertex)
{
  Vertice *adjList = &D->V[vertex];
  Vertice *temp = adjList;

  if (D->V[vertex].visitado == 1)
  {
    return;
  }
  else
  {
    D->V[vertex].visitado = 1;
  }

  for (Arco *a = temp->arcos_saida; a != NULL; a = a->prox)
  {
    int vizinho = a->fim;
    DFS(D, vizinho);
  }
}

void dfs_DFS(Digrafo *D, int vertex, int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    D->V[i].visitado = 0;
  }
  DFS(D, 0);
}
// DFS-------------------------------------------------------------

// Funcao para retornar se vizinho tem um vizinho de mesma cor
// Funciona/não mudar
int vizinho_cor(Digrafo *D, int index)
{
  int cor_origem, vizinho;
  Vertice *adjList = &D->V[index];
  Vertice *temp = adjList;

  cor_origem = D->V[index].cor;

  for (Arco *a = temp->arcos_saida; a != NULL; a = a->prox)
  {
    vizinho = a->fim;
    if (D->V[vizinho].cor == cor_origem && D->V[vizinho].visitado == 0)
    {
      return 1;
    }
  }
  return 0;
}

void vizinho_DFS(Digrafo *D, int id, int *cor_vec)
{
  int cor = D->V[id].cor;
  for (Arco *a = D->V[id].arcos_saida; a != NULL; a = a->prox)
  {
    int vizinho = a->fim;
    if (D->V[vizinho].cor == cor && D->V[vizinho].visitado == 0)
    {
      cor_vec[D->V[vizinho].cor] += 1;
      D->V[vizinho].visitado = 1;
      vizinho_DFS(D, vizinho, cor_vec);
    }
  }
  return;
}
// Checa_vizinho é basicamente um DFS limitado---------------------------------
void busca_vizinho(Digrafo *D, int index, int *cor_vec)
{
  Vertice *adjList = &D->V[index];
  Vertice *temp = adjList;

  if (D->V[index].visitado == 1)
  {
    return;
  }
  else
  {
    D->V[index].visitado = 1;
  }
  int vizinho;
  for (Arco *a = temp->arcos_saida; a != NULL; a = a->prox)
  {
    vizinho = a->fim;
    if (D->V[vizinho].visitado == 0 && D->V[vizinho].ramo_principal == 0)
    {
      cor_vec[D->V[vizinho].cor] += 1;
      D->V[vizinho].visitado = 1;
      if (vizinho_cor(D, vizinho) == 1)
      {
        // printf("\nRetorno %d\n", D->V[vizinho].cor);
        vizinho_DFS(D, vizinho, cor_vec);
      }
    }
  }
  return;
}
void checa_vizinho(Digrafo *D, int index, int cor_vec[], int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    D->V[i].visitado = 0;
  }
  for (i = 0; i < 6; i++)
  {
    cor_vec[i] = 0;
  }
  for (i = 0; i < n; i++)
  {
    if (D->V[i].ramo_principal == 1)
      busca_vizinho(D, i, cor_vec);
  }
}
// Checa_vizinho é basicamente um DFS limitado---------------------------------

int escolha_cor(int *cor_vec, int *cor_total)
{
  int i, aux = 0, maior = -1230000;

  // int cor_candidato[6] = {0};
  // int status = 0;
  for (i = 0; i < 6; i++)
  {
    if (cor_vec[i] == cor_total[i] && cor_total[i] != 0)
    {
      cor_total[i] = 0;
      return i;
    }

    if (cor_vec[i] > maior)
    {
      // if(cor_vec[i] == maior)
      // {
      //   status = 1;
      //   cor_candidato[i]++;
      // }
      maior = cor_vec[i];
      aux = i;
    }
  }

  // if(status == 1)
  // {
  //   for(i = 0; i < 6; i++)
  //   {
  //     if((cor_total[i] > x) && (cor_candidato[i] == 1))
  //     {
  //       x = cor_total[i];
  //       aux = i;
  //     }
  //   }
  //   printf("\n\nEscolhi a cor: %d\n\n", aux);
  // }
  cor_total[aux] -= maior;

  return aux;
}

// Trab01 do Hokama termina aqui---------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------

// Trab02 do Hokama começa aqui----------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
// Numero de cores
int limitante_inferior = 6;

// Heuristica
int limitante_superior;

// Vetor de cores
int vec[6];

// Soma de verificação de cores
int sum;

// Flag para soma de verificação
int flag;

int cor_poda[6];

int cor_candidato[6];

void reseta_grafo(int *sequencia_cores, Digrafo *Aux, int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    Aux->V[i].cor = sequencia_cores[i];
  }
}

int testa_solucao(int *vec_solucao, int tam, Digrafo *Aux, int *sequencia_cores, int *cor_vec, int n)
{
  for (int i = 0; i < tam; i++)
  {
    // printf("tamanho: %d ", tam);
    muda_cor(Aux, 0, vec_solucao[i], cor_vec);
    ramo_DFS(Aux, 0, n);
  }

  // retorna 1 se funcionar
  if (verifica_fim(Aux))
  {
    // printf("Sucesso!\n");
    reseta_grafo(sequencia_cores, Aux, n);
    return 1;
  }
  // ou zero se falhar
  else
  {
    // printf("Falha\n");
    reseta_grafo(sequencia_cores, Aux, n);
    return 0;
  }
}

int verifica;

void bnb(int posicaoAT, int *vet, Digrafo *Aux, int *sequencia_cores, int *cor_vec, int n, int *vec_solucao)
{
  int cont;

  // Testa solução para o grafo auxiliar
  if (posicaoAT >= limitante_inferior && !flag)
  {
    if (testa_solucao(vet, posicaoAT, Aux, sequencia_cores, cor_vec, n))
    {
      verifica = 1;
      limitante_superior = posicaoAT;

      for (int i = 0; i < posicaoAT; i++)
      {
        vec_solucao[i] = vet[i];
        // printf("%d ", vec_solucao);
      }
    }
    return;
  }

  // Poda as sequencias de tamanho igual ao limite superior
  if (posicaoAT >= limitante_superior - 1)
  {
    return;
  }
  checa_vizinho(Aux, 0, cor_vec, n);
  // Geraçao de sequencias
  for (int cont = 0; cont < limitante_inferior; cont++)
  {
    flag = 0;
    if (posicaoAT > 0 && vet[posicaoAT - 1] == cont)
      continue;

    if (cor_vec[cont] == 0)
    {
      // printf("Valor do cont: %d\n", cont);
      // printf("R|O|P|Y|G|C\n");
      // for (int i = 0; i < 6; i++) {
      //   printf("%d|", cor_vec[i]);
      // }
      // printf("\n\n");
      continue;
    }
    vet[posicaoAT] = cont;
    bnb(posicaoAT + 1, vet, Aux, sequencia_cores, cor_vec, n, vec_solucao);
  }
  return;
}

// Trab02 do Hokama Termina aqui---------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------
//--------------------------------------------------------------

void resolvedor(char *entrada_filename, char *solucao_filename)
{

  FILE *entrada_file = fopen(entrada_filename, "r");
  if (entrada_file == NULL)
  {
    printf("Meu erro ao abrir arquivo de entrada!\n");
  }

  // Lendo entrada
  int n, m, i;
  fscanf(entrada_file, "%d %d", &n, &m);
  Digrafo *D = criar_grafo(n);
  Digrafo *Aux = criar_grafo(n);

  int cor_vec[6]; // Vetor auxiliar para checar cores de vizinhos
  for (i = 0; i < 6; i++)
    cor_vec[i] = 0;
  int cor_total[6]; // Soma de todas as cores
  for (i = 0; i < 6; i++)
    cor_total[i] = 0;
  int *sequencia_cores = (int *)malloc(sizeof(int) * n);

  for (int v = 0; v < n; v++)
  {
    int cor;
    fscanf(entrada_file, "%d", &cor);

    // Contabiliza o total de cores
    if (v > 0)
      cor_total[cor] += 1;

    // Armazena a sequencia de cores
    sequencia_cores[v] = cor;

    seta_cor(D, v, cor);
    seta_cor(Aux, v, cor);
  }

  for (int e = 0; e < m; e++)
  {
    int ini, fim;
    fscanf(entrada_file, "%d %d", &ini, &fim);
    adiciona_arco(D, ini, fim);
    adiciona_arco(Aux, ini, fim);
  }
  fclose(entrada_file);
  //***************************

  // *** Resolvendo de fato (de maneira tosca) **
  // vou criar um vetor para guardar os movimentos
  // estou chutando um numero enorme de n*n*6
  // espero usar menos
  int max_movimentos = n * n * 6;
  int *movimentos = (int *)malloc(sizeof(int) * max_movimentos);
  int *vec_bnb = (int *)malloc(sizeof(int) * max_movimentos);
  int *vec_solucao = (int *)malloc(sizeof(int) * max_movimentos);
  int num_movimentos = 0;

  i = 0;
  int aux = 0;

  // Enquanto naum deixar todos os nos da mesma cor.
  // Aqui ocorre o calculo da heuristica
  while (verifica_fim(D) != 1)
  {
    checa_vizinho(D, 0, cor_vec, n);

    // Imprimir
    // printf("Vetor de cores:\n");
    // printf("R|O|P|Y|G|C\n");
    // for(i = 0; i < 6; i++)
    // {
    //     printf("%d|", cor_vec[i]);
    // }
    // printf("\n\n");

    aux = escolha_cor(cor_vec, cor_total);
    movimentos[num_movimentos] = aux;

    muda_cor(D, 0, movimentos[num_movimentos], cor_vec);
    ramo_DFS(D, 0, n);

    num_movimentos++;

    // printf("Vetor de cores totais:\n");
    // printf("R|O|P|Y|G|C\n");
    // for(i = 0; i < 6; i++)
    //{
    //     printf("%d|", cor_total[i]);
    // }
    // printf("\n-----------------------\n\n");
  }

  verifica = 0;
  limitante_superior = num_movimentos;

  bnb(0, vec_bnb, Aux, sequencia_cores, cor_vec, n, vec_solucao);

  libera_digrafo(D);

  //*** Escrevendo arquivo de solucao ***
  FILE *solucao_file = fopen(solucao_filename, "w");
  if (solucao_file == NULL)
  {
    printf("Meu erro ao abrir arquivo de solucao!\n");
  }

  if (!verifica)
  {
    fprintf(solucao_file, "%d\n", limitante_superior);
    for (int i = 0; i < limitante_superior; i++)
    {
      fprintf(solucao_file, "%d ", vec_solucao[i]);
    }
    fprintf(solucao_file, "\n");
  }
  else
  {
    fprintf(solucao_file, "%d\n", num_movimentos);
    for (int i = 0; i < num_movimentos; i++)
    {
      fprintf(solucao_file, "%d ", movimentos[i]);
    }
    fprintf(solucao_file, "\n");
  }

  fclose(solucao_file);

  free(movimentos);
  return;
}
