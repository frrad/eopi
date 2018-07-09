def int_sqrt(n):
    def func(L, U):
        M = (L + U) // 2
        if M**2 > n:
            if M == L:
                return L-1
            return func(L, M)
        return func(M+1, U)
    return func(0, n+1)
