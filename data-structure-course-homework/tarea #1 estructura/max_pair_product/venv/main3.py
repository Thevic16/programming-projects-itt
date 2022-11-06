def max_element(a):
    # Get length of array
    n = len(a)
    # Init max element to first element
    m = a[0]
    # Iterate over all remainning elements
    for i in range(1, n ):
        # Get value of element
        print(i)
        val = a[i]
        # Check new max element
        if val > m:
            # Set new max product
            m = val
    # Return max product
    return m


def main():
    a = [2,5,6,4,100,2,3,4,10,300]
    print(max_element(a))



main()