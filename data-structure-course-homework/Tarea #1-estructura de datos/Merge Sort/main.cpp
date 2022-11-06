/* C program for Merge Sort */
#include<stdlib.h>
#include<stdio.h>


// El primer subarray es a [n]
// El segundo subarray es a [n]

void merge(int a[],size_t n, int b[], size_t m,int c[])
{
    int i = 0; // Índice inicial de la primera submatriz
    int j = 0; // Índice inicial de la segunda submatriz
    int k = 0; // Índice inicial de subarreglos fusionados
    while (i < n && j < m) // mientras halla algun indice por debajo del tamaño del arreglo
    {
        if (a[i] <= b[j])  // Si a[i] es menor o igual que b[j], almacenar a[i] en el arreglo (c)
        {
            c[k] = a[i];
            i++;            // se evalua a (a) en la siguiente posición.
        }
        else       // Si a[i] es mayor que b[j], almacenar b[j] en el arreglo (c)
        {
            c[k] = b[j];
            j++;           // se evalua a (b) en la siguiente posición.
        }
        k++;               //siempre se aumenta el indice de (c)
    }
    /* Copiar los elementos restantes de a [], si queda
     * alguno*/
    while (i < n)
    {
        c[k] = a[i];
        i++;
        k++;
    }

    /* Copiar los elementos restantes de b [], si queda
     * alguno*/
    while (j < m)
    {
        c[k] = b[j];
        j++;
        k++;
    }
}



/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */


int main()
{
    int a[]  = {5, 7, 12, 16};
    int n = 4;
    int b[] = {1, 3, 6, 9, 11, 15, 17, 18};
    int m = 8;

    int c[100];

    merge(a,n,b,m,c);

    printArray(c,n+m);

    return 0;
}
