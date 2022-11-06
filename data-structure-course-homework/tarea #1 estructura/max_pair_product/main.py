
def max_pair_product(a):
    # Get length of array
    n = len(a)
    # Init max product to multiplicaction of first two elements
    max_product = a[0] * a[1]
    # Iterate over all elements (except last)
    for i in range(n - 1):
        # Get value of element
        val_1 = a[i]
        # Create all possible combinations with above element
        for j in range(i + 1, n):
            # Compute product
            current_product = a[i] * a[j]
            # Check new max product
            if current_product > max_product:
                # Set new max product
                max_product = current_product

    # Return max product
    return max_product


def main():
    a = [10,2,3,5,4,6,10]
    print(max_pair_product(a))




main()