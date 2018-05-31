def wrong(input):
    return input


def wronger(input):
    return [[3, 1], [4, 2]]


def rotate_90_clock_np(arr):
    import numpy as np
    arr = np.array(arr)
    arr_rot = np.zeros(arr.shape)
    for old_row_ind, new_col_ind in enumerate(range(len(arr))[::-1]):
        arr_rot[:, new_col_ind] = arr[old_row_ind, :]
    return arr_rot.astype(int).tolist()


def rotate_90_clock(arr):
    n = len(arr)
    arr_rot = [[None] * n for i in range(n)]
    for old_row_ind, new_col_ind in enumerate(range(n)[::-1]):
        for old_col_ind, new_row_ind in enumerate(range(n)):
            arr_rot[new_row_ind][new_col_ind] = arr[old_row_ind][old_col_ind]
    return arr_rot
