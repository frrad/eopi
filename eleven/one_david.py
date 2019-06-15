def find_first_occurence_ind(arr, key):
    ceil = len(arr)
    floor = 0
    keep_searching = True

    while keep_searching:
        test_ind = (floor + ceil) // 2
        test_val = arr[test_ind]
        if test_ind in (floor, ceil):
            keep_searching = False

        if test_val >= key:
            ceil = test_ind
        else:
            floor = test_ind

    return ceil