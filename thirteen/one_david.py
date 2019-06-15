def find_intersection(arr1, arr2):
    ind1 = 0
    ind2 = 0
    intersect_vals = []

    while ind1 < len(arr1) and ind2 < len(arr2):
        if arr1[ind1] == arr2[ind2]:
            if len(intersect_vals) == 0 or arr1[ind1] > intersect_vals[-1]:
                intersect_vals.append(arr1[ind1])
            ind1 += 1
            ind2 += 1
        elif arr1[ind1] > arr2[ind2]:
            ind2 += 1
        else:
            ind1 += 1

    return intersect_vals