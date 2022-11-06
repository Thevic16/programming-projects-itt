def max_pair_product(a):
    # Get length of array
    n = len(a)
    # create two variables to store the major and the second major
    mayor = 0
    segundo_mayor = 0

    # Iterate over all elements and make place comparisons
    for i in range(n):
        if(a[i] > segundo_mayor):
            segundo_mayor = a[i]
            if(segundo_mayor>mayor):
                temp = mayor
                mayor = segundo_mayor
                segundo_mayor = temp


    # Return max product
    return mayor*segundo_mayor


def main():
    #a = [10,2,3,5,4,6,10]
    #a = [10, 2, 3, 1, 4, 6, 10]

    a = [8, 8, 3, 1, 4, 6, 6]
    a = [1, 2, 3, 9, 4, 19, 6]
    print(max_pair_product(a))




main()