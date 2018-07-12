def merge_arrays(arr1, arr2):
    # Get size of arrays
    num1 = 0
    for val in arr1:
        if val == '_':
            break
        num1 += 1
    num2 = 0
    for val in arr2:
        if val == '_':
            break
        num2 += 1
    
    # Merge starting from the back
    while num1 > 0 and num2 > 0:
        val1 = arr1[num1 - 1]
        val2 = arr2[num2 - 1]

        if val1 > val2:
            arr1[num1 + num2 - 1] = val1
            num1 -= 1
        else:
            arr1[num1 + num2 - 1] = val2
            num2 -= 1
    
    # Add the remainder of the second array if necessary
    if num2 > 0:
        arr1[:num2] = arr2[:num2]