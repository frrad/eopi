def first_of(arr, x):
    def func(L, U):
        M = (L+U)//2
        if arr[M] == x:
            if L == M: 
                return M 
            else:
                return func(L, M)
        elif arr[M] < x:
            return func(M+1, U)
        else:
            return func(L, M-1)
    return func(0, len(arr)-1)
