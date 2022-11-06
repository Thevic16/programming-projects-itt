// C++ program to implement three way partitioning 
// around a given range. 
#include<iostream>
using namespace std;

/*
// Particiones arr[0..n-1]
void threeWayPartition(int arr[], int n,int pivot)
{
    // Inicializa las posiciones disponibles para
    // elementos más pequeños (que el rango) y mayores
    int start = 0, end = n-1;

    // Elementos transversales desde la izquierda
    for (int i=0; i<=end;)
    {
        // Si el elemento actual es más pequeño que
        // pivote, se pone en el siguiente disponible más pequeño
        // posición.
        if (arr[i] < pivot){
            swap(arr[i], arr[start]);
            i++;
            start++;
        }
        // Si el elemento actual es mayor que
        // pivote,se pone en el siguiente disponible mayor
        // posición.
        else if (arr[i] > pivot){
            swap(arr[i], arr[end]);
            end--;
        }

        else
            i++;
    }
}
*/

void partition(int a[], int n)
{
    int pivot = a[n-1];
    size_t smaller_idx = 0;
    size_t larger_idx = n-1;
    for (size_t idx = 0; idx <= larger_idx;)
    {
        if (a[idx] < pivot)
        {
            swap(a[idx], a[smaller_idx]);
            //a[smaller_idx] = a[idx];
            smaller_idx++;
            idx++;
        }
        else if (a[idx] > pivot)
        {
            swap(a[idx], a[larger_idx]);
            //a[larger_idx] = a[idx];
            larger_idx--;
        }
        else{
            idx++;
        }

    }
    //size_t pivot_idx = smaller_idx;
    //a[pivot_idx] = pivot; // -> O(1)
   // return pivot_idx; // -> O(1)
}


// Driver code 
int main()
{
    int arr[] = {5, 2, 4, 1, 3, 7, 0, 9,7};
    int n = sizeof(arr)/sizeof(arr[0]);

    //threeWayPartition(arr, n,9);

    partition(arr,n);

    cout << "Modified array \n";
    for (int i=0; i<n; i++)
        cout << arr[i] << " ";
} 
