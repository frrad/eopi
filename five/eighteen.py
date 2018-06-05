def change_direction(increment):
    increment_new = increment[::-1]
    if abs(increment[0]) == 1:
        increment_new[1] *= -1
    return increment_new


def spiralize(arr):
    i_bounds = [0, len(arr) - 1]
    j_bounds = [0, len(arr[0]) - 1]
    increment = [0, 1]
    i = 0
    j = 0
    arr_spiral = []

    while i_bounds[1] >= i_bounds[0]:

        arr_spiral.append(arr[i][j])

        i_prop = i + increment[0]
        j_prop = j + increment[1]

        if j_prop > j_bounds[1]:
            i_bounds[0] += 1
        elif j_prop < j_bounds[0]:
            i_bounds[1] -= 1
        elif i_prop > i_bounds[1]:
            j_bounds[1] -= 1
        elif i_prop < i_bounds[0]:
            j_bounds[0] += 1
        else:
            i = i_prop
            j = j_prop
            continue

        increment = change_direction(increment)
        i += increment[0]
        j += increment[1]

    return arr_spiral
