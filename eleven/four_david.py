def compute_int_sqrt(num):
    floor = 0
    ceil = num
    int_sqrt = 0
    keep_searching = True

    while keep_searching:
        test_val = (ceil + floor + 1) // 2
        if test_val in (floor, ceil):
            keep_searching = False

        if test_val**2 > num:
            ceil = test_val
        else:
            floor = test_val
            int_sqrt = test_val

    return int_sqrt