//Lucas Batista Pereira
//Árvore Binária Básica
//22/06/2021

#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
  int key;
  struct Node *left, *right;
  int n;
}Node;

void insert(Node **root, int key);
void InOrder(Node *root);
void PreOrder(Node *root);
void PostOrder(Node *root);
Node* Delete(Node **x, int key);
Node* BuscaMinimo(Node *root);
Node* put(Node **x, int key);
int size(Node *x);
void Free(Node **x);

int main(void)
{
  Node *root = NULL;
  int saida = 0, menu, key;

  while(saida < 1)
  {
    system("clear");
    printf("\n1 - Inserção\n");
    printf("2 - Remoção\n");
    printf("3 - Mostrar percurso Ordenado\n");
    printf("4 - Mostrar percurso Pré-Ordem\n");
    printf("5 - Mostrar percurso Pós-Ordem\n");
    printf("0 - Encerrar programa\n");
    scanf("%i", &menu);
    if(menu >= 0 && menu <= 5)
    {
      switch(menu)
      {
        case 1:
        system("clear");
        printf("Digite o valor a ser inserido\n");
        scanf("%i", &key);
        insert(&root, key);
        break;

        case 2:
        system("clear");
        if(!root){printf("Árvore não exite!");break;}
        printf("Digite o valor a ser deletado:\n");
        scanf("%i", &key);
        Delete(&root, key);
        break;

        case 3:
        if(!root){printf("Árvore não exite!");break;}
        InOrder(root);
        break;

        case 4:
        if(!root){printf("Árvore não exite!");break;}
        PreOrder(root);
        break;

        case 5:
        if(!root){printf("Árvore não exite!");break;}
        PostOrder(root);
        break;

        case 0:
        system("clear");
        if(!root){printf("Árvore não exite!");break;}
        Free(&root);
        printf("Árvore apagada!\n");
        saida++;
        break;
      }
    }else{printf("Entrada invalida!");}

  }
  return 0;
}


void insert(Node **root, int key)
{
  (*root) = put(&(*root), key);
}

Node* put(Node **x, int key)
{
 if(!(*x))
 {
 (*x) = (Node *)malloc(sizeof(Node));
 (*x)->key = key;
 (*x)->left = (*x)->right = NULL;
 (*x)->n = 1;
 return (*x);
 }
 if(key < (*x)->key)
 (*x)->left = put(&(*x)->left, key);
 else
 (*x)->right = put(&(*x)->right, key);

 (*x)->n = 1 + size((*x)->left) + size((*x)->right);

return (*x);
}

int size(Node *x)
{
 if(!x) return 0;
 else return x->n;
}

void InOrder(Node *root)
{
   if (root != NULL)
   {
      InOrder(root->left);
      printf("%d ", root->key);
      InOrder(root->right);
   }
}

void PreOrder(Node *root)
{
   if (root != NULL)
   {
      printf("%d ", root->key);
      PreOrder(root->left);
      PreOrder(root->right);
   }
}

void PostOrder(Node *root)
{
   if (root != NULL)
   {
      PostOrder(root->left);
      PostOrder(root->right);
      printf("%d ", root->key);
   }
}
void Free(Node **x)
{
   if ((*x) != NULL)
   {
      Free(&(*x)->left);
      Free(&(*x)->right);
      free((*x));
   }else return;
}

Node* Delete(Node **x, int key)
{
  if((*x) == NULL) return (*x);
  else if(key < (*x)->key)
  {(*x)->left = Delete(&(*x)->left, key);}
  else if(key > (*x)->key)
  {(*x)->right = Delete(&(*x)->right, key);}
  else
  {
    if((*x)->right == NULL && (*x)->left == NULL)
    {
      free(*x);
      (*x) = NULL;
    }
    else if((*x)->right == NULL)
    {
      Node *temp;
      temp = (*x)->left;
      free(temp);
    }
    else if((*x)->left == NULL)
    {
      Node *temp;
      temp = (*x)->right;
      free(temp);
    }
    else
    {
      Node *temp = BuscaMinimo((*x)->right);
      (*x)->key = temp->key;
      (*x)->right = Delete(&(*x)->right, temp->key);
    }
  }
  return (*x);
}

Node* BuscaMinimo(Node *root)
{
  if(root == NULL){printf("Árvore não exite\n");return NULL;}
  while(root->left != NULL){root = root->left;}
  return root;
}
