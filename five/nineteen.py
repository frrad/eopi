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


def rotate_coords_90_clock(i, j, n):
    i_rot = j
    j_rot = n - 1 - i
    return i_rot, j_rot


def rotate_corners(arr, i_start, j_start):
    n = len(arr)
    i_orig, j_orig = i_start, j_start
    reassign_val = arr[i_orig][j_orig]
    for _ in range(4):
        i_rot, j_rot = rotate_coords_90_clock(i_orig, j_orig, n)
        temp = arr[i_rot][j_rot]
        arr[i_rot][j_rot] = reassign_val
        reassign_val = temp
        i_orig, j_orig = i_rot, j_rot

        
def rotate_square(arr, ind_start):
    i_start = ind_start
    for j_start in range(ind_start, len(arr) - ind_start - 1):
        rotate_corners(arr, i_start, j_start)

        
def rotate_90_clock_inplace(arr):
    num_square = len(arr) / 2
    for ind_start in range(num_square):
        rotate_square(arr, ind_start)
    return arr

        
def rotate_90_clock(arr):
    n = len(arr)
    arr_rot = [[None] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            i_rot, j_rot = rotate_coords_90_clock(i, j, n)
            arr_rot[i_rot][j_rot] = arr[i][j]
    return arr_rot
