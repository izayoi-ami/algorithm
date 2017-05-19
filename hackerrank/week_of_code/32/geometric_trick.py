##
from functools import wraps

def memoize(f):
    memo = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        try: return memo[args]
        except KeyError:
            memo[args] = f(*args, **kwargs)
            return memo[args]
    return wrapper

@memoize
def squarefree_part(n):
    from math import sqrt
    if n==1: return 1
    if n&1==0:
        cnt = 0
        while n&1==0:
            n >>= 1
            cnt += 1
        return 2**(cnt&1) * squarefree_part(n)
    p=3
    M = int(sqrt(n))
    while p <= M:
        cnt = 0
        while n%p == 0:
            n//=p
            cnt += 1
        if cnt: return p**(cnt&1) * squarefree_part(n)
        p += 2
    return n

def geometricTrick(s):
    from math import sqrt
    N = len(s)
    cnt = 0
    for i,v in enumerate(s):
        if v in "ac":
            a=i+1
            sq = squarefree_part(a)
            p = int(sqrt(a//sq))
            start = p + 1
            while sq*start**2 <= N:
                j, k = sq*p*start-1, sq*start**2-1
                if s[j] == "b":
                    if s[k]=="a" and v=="c" or s[k]=="c" and v=="a":
                        cnt+=1
                start += 1
    return cnt

# n = int(input().strip())
# s = input().strip()
# result = geometricTrick(s)
# print(result)        

##
