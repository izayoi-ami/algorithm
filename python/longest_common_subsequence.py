##
from functional import memoize

@memoize
def LCS_compact(x,y):
    def delta(a,b):
        if x[a]==y[b]: return 1
        return 0
    m,n = len(x), len(y)
    if m == 0 or n == 0: return 0
    ans = [[0] * (n) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            prev = delta(i,j) + ( (ans[i-1][j-1]) if i>0 and j>0 else 0)
            prev_1 = ans[i-1][j] if i>0 else 0
            prev_2 = ans[i][j-1] if j>0 else 0
            ans[i][j] = max(prev, prev_1, prev_2)
    return ans

def backtrack(s1,s2, ans):
    def val(point):
        x,y = point
        return ans[x][y]

    s = []
    point = (len(s1),len(s2))
    while point != (0,0):
        x,y = point
        corner = (x-1,y-1)
        up = (x-1, y)
        left = (x, y-1)
        if val(corner) < val(point):
            s.append(s1[x-1])
            point = corner
        elif val(point) == val(left):
            point = left
        else:
            point = up

    res = "".join(s)[::-1]
    return res


def LCS(x,y):
    def delta(a,b):
        return 1 if a == b else 0

    def take(arr, point):
        x,y = point
        return arr[x][y]
    
    m, n = len(x), len(y)
    if m == 0 or n == 0: return 0
    a = [[0] *(n+1) for _ in range(m+1)]

    for i,v in enumerate(x, start = 1):
        for j,w in enumerate(y, start=1):
            a[i][j] = max(a[i-1][j], a[i][j-1], delta(v,w) + a[i-1][j-1])
        
    return backtrack(x,y,a), a

##

def longest_common_substring(s1,s2):
    N = len(s2)
    prev = [0] * (N+1)
    best = 0
    pos = (-1,-1)
    for i,v in enumerate(s1):
        curr = [0] * (N+1)
        for j,w in enumerate(s2, start=1):
            if v==w: 
                curr[j] = prev[j-1] + 1
                if curr[j] > best: best, pos = curr[j], (i,j)
            else: curr[j] = 0
        prev = curr
    b, p = best, pos
    s = []
    while b > 0:
        i, j = p 
        s.append(s1[i])
        b -=1
        p = (i-1, j-1)
    res = "".join(s)[::-1]
    return res, best, pos

##

