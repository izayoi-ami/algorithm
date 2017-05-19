##
def longest_common_subsequence(A,B):
    def val(pos):
        i,j = pos
        return a[i][j]
    M, N = len(A), len(B)
    a = [[0]*(N+1) for _ in range(M+1)]
    # back = [[None] *(N+1) ] * (M+1)
    for i,v in enumerate(A,start=1):
        for j,w in enumerate(B,start=1):
            delta = 1 if v==w else 0
            a[i][j] = max(a[i-1][j], a[i][j-1], delta*(1+ a[i-1][j-1]))
        # print("\n".join(map(repr,a)))
        # print()
    pos = (M,N)
    s = []
    while 0 not in pos:
        i,j = pos
        up = (i-1,j)
        left = (i-1, j-1)
        corner = (i-1,j-1)
        vp, vu, vl, vc = map(val,[pos,up,left,corner])
        if vp == vu:
            pos = up
        elif vp == vl:
            pos = left
        else:
            s.append(A[corner[0]])
            pos = corner
    res = s[::-1]
    return res, a

def solution():
    n, m = [int(v) for v in input().rstrip().split(" ")]
    A = [int(v) for v in input().rstrip().split(" ")]
    B = [int(v) for v in input().rstrip().split(" ")]
    ans, table = longest_common_subsequence(A,B)
    print(" ".join(map(str,ans)))
##
