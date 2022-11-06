#Versión de Python usada: Python 3.7.1
def selection_sort_mejorado(A):

    n=len(A)
    cont =0 #contador

    # Recorrer todos los elementos del arreglo
    for i in range(n):

        # Encuentra el elemento mínimo en el resto
        # matriz sin clasificar
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

            if A[j-1]<A[j]: #Sí estos elementos estan el orden
                cont = cont +1 # el contador aumenta
                if cont == n-i-1: # se compara cont con lo que resta del arreglo
                    return A

        # Intercambie el elemento mínimo encontrado con
        # el primer elemento del rango evaluado.
        A[i], A[min_idx] = A[min_idx], A[i]

        cont = 0 #Se reinicia el contador para volver

                 #a verificar en la siguiente pasada
    return A


def main():
    #A = [64, 25, 12, 22, 11]
    #A = [11, 12, 22, 25, 64]
    #A = [7,8,5,4,9,2]
    A = [23, 78, 45 ,8, 32, 56, 1 ]
    # Probando el algoritmo.
    print("Arreglo ordenado")
    A = selection_sort_mejorado(A)
    for i in range(len(A)):
        print(A[i])


main()