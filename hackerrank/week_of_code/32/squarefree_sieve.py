##

def squarefree_list(N):
    from math import sqrt
    L = list(range(N+1))
    for i in range(1,N+1):
        if L[i] == i:
            M=int(sqrt((N+1)//i))
            for j in range(2,M+1):
                L[i*j**2] = i
    return L




##
