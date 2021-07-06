#include <stdio.h>
#include <stdlib.h>


typedef struct Node{
  int key;
  struct Node *left;
  struct Node *right;
  int n;
  int height;
}Node;

int max(int a, int b);
Node* balance(Node **x);
int balanceFactor(Node *x);
int height(Node *x);
void insert(Node **root, int key);
Node* put(Node **x, int key);
Node* rotateLeft(Node *h);
Node* rotateRight(Node *h);
int size(Node *x);
Node* Delete(Node **x, int key);
Node* BuscaMinimo(Node *root);
void InOrder(Node *root);
void PreOrder(Node *root);
void PostOrder(Node *root);
void Free(Node **x);
void search(Node *node, int key);
int searchFB(Node *node, int key);


int main(void)
{
  Node *root = NULL;
  int saida = 0, menu, key;

  while(saida < 1)
  {
    scanf("%i", &menu);
    if(menu >= 1 && menu <= 8)
    {
      switch(menu)
      {
        case 1:
        scanf("%i", &key);
        insert(&root, key);
        break;

        case 2:
        scanf("%i", &key);
        search(root, key);
        break;

        case 3:
        scanf("%i", &key);
        Delete(&root, key);
        break;

        case 4:
        PreOrder(root);
        printf("\n");
        break;

        case 5:
        InOrder(root);
        printf("\n");
        break;

        case 6:
        PostOrder(root);
        printf("\n");
        break;

        case 7:
        scanf("%d", &key);
        printf("%d\n",searchFB(root, key));
        break;

        case 8:
        Free(&root);
        saida++;
        break;
      }
    }
  }
  return 0;
}

int max(int a, int b)
{
    return (a > b)? a : b;
}

Node* balance(Node **x)
{
    if(balanceFactor((*x)) < -1)
    {
        if(balanceFactor((*x)->right) > 0)
            (*x)->right = rotateRight((*x)->right);
        (*x) = rotateLeft((*x));
    }
    else if(balanceFactor((*x)) > 1)
    {
        if(balanceFactor((*x)->left) < 0)
            (*x)->left = rotateLeft((*x)->left);
        (*x) = rotateRight((*x));
    }
    return (*x);
}

int balanceFactor(Node *x)
{
    return height(x->left) - height(x->right);
}

int height(Node *x)
{
    if(!x) return -1;
    return x->height;
}

void insert(Node **root, int key)
{
    put(&(*root), key);
}

Node* put(Node **x, int key)
{
    if(!(*x))
    {
        (*x) = (Node *)malloc(sizeof(Node));
        (*x)->key = key;
        (*x)->left = (*x)->right = NULL;
        (*x)->n = 1;
        (*x)->height = 0;
        return (*x);
    }

    if(key < (*x)->key)
        put(&(*x)->left, key);
    else
        put(&(*x)->right, key);

    (*x)->n = 1 + size((*x)->left) + size((*x)->right);
    (*x)->height = 1 + max(height((*x)->left), height((*x)->right));

    return balance(&(*x));
}

Node* rotateLeft(Node *h)
{
    Node *x = h->right;
    h->right = x->left;
    x->left = h;
    x->n = h->n;
    h->n = 1 + size(h->left) + size(h->right);
    h->height = 1 + max(height(h->left), height(h->right));
    x->height = 1 + max(height(x->left), height(x->right));
    return x;
}

Node* rotateRight(Node *h)
{
    Node *x = h->left;
    h->left = x->right;
    x->right = h;
    x->n = h->n;
    h->n = 1 + size(h->left) + size(h->right);
    h->height = 1 + max(height(h->left), height(h->right));
    x->height = 1 + max(height(x->left), height(x->right));
    return x;
}

int size(Node *x)
{
    if(!x) return 0;
    return x->n;
}

Node* Delete(Node **x, int key)
{
    if ((*x) == NULL)
        return (*x);

    if ( key < (*x)->key )
        (*x)->left = Delete(&(*x)->left, key);

    else if( key > (*x)->key )
        (*x)->right = Delete(&(*x)->right, key);

    else
    {
        if( ((*x)->left == NULL) || ((*x)->right == NULL) )
        {
            Node *temp = (*x)->left ? (*x)->left : (*x)->right;
            if (temp == NULL)
            {
                temp = (*x);
                (*x) = NULL;
            }
            else *(*x) = *temp;

            free(temp);
        }
        else
        {
            Node* temp = BuscaMinimo((*x)->right);

            (*x)->key = temp->key;

            (*x)->right = Delete(&(*x)->right, temp->key);
        }
    }

    if ((*x) == NULL)return (*x);

  (*x)->n = 1 + size((*x)->left) + size((*x)->right);
  (*x)->height = 1 + max(height((*x)->left), height((*x)->right));

  return balance(&(*x));
}

Node* BuscaMinimo(Node *root)
{
  if(root == NULL){//printf("Árvore não exite\n");
  return NULL;}
  while(root->left != NULL){root = root->left;}
  return root;
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

void search(Node *node, int key)
{
   if (key < node->key)
        search(node->left, key);
    else if (key > node->key)
        search(node->right,key);
    else if (key == node->key)
        {printf("%d\n", node->key); return;}

    printf("x\n");
    return;
}

int searchFB(Node *node, int key)
{
   if (key < node->key)
        searchFB(node->left, key);
    else if (key > node->key)
        searchFB(node->right, key);
    else if (key == node->key) return balanceFactor(node);
    return 0;
}

