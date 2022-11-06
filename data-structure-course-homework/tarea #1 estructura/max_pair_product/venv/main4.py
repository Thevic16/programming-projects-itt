#Versión de Python usada: Python 3.7.1
def maxima_ganancia_bolsa(a):
    n = len(a)
    b = []  #nuevo arreglo transformado

    for i in range(1,n):
        b.append(a[i]-a[i-1]) #añadiendo los elementos transformados

    return max_subSum(b) #retornar la maxima suma sub-arreglo de (b)


def max_subSum(a):

    n=len(a) #Toma el tamaño de el arreglo (a).
    max_suma =0  #Contenedor de la suma, para efectuar
                 #las comparaciones.

    suma =0      #Almacenara la suma en cada ejecución
                 #del doble for.

    for i in range(n):
        for j in range(i,n):
            suma = suma + a[j] # Suma los elementos en el rango especificado.

            if suma > max_suma:  # Compara la suma actual con la anterior
                max_suma = suma

        suma =0

    return  max_suma







def main():
    a = [1, 3, 13,6]
    print(maxima_ganancia_bolsa(a))



main()