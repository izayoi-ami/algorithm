##
def binary_search(A, target, lo=0, hi=None):
    if hi is None: hi=len(A)
    while lo<=hi:
        mid = (lo+hi)//2
        if A[mid] == target: return mid
        if A[mid] > target: hi = mid - 1
        else: lo = mid + 1
    return -1
##

def binary_upper_bound(A, target, lo=0, hi=None):
    """
    return max index such that A[index]<=target
    """
    if hi is None: hi=len(A)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if A[mid] > target: hi = mid - 1
        else: lo = mid + 1
    return lo-1
##

def binary_lower_bound(A, target, lo=0, hi=None):
    """
    return min index such that A[index]>=target
    """
    if hi is None: hi=len(A)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if A[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return hi+1
##
def set_ceil(A, target):
    lo, hi = 0, len(A)
    while lo < hi:
        mid = (lo+hi)//2
        if A[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return hi

def set_floor(A, target):
    lo, hi = 0, len(A)
    while lo < hi:
        mid = (lo+hi)//2
        if A[mid] > target:
            hi = mid
        else:
            lo = mid + 1

    return lo-1




##
def local_minimum(A, lo=0, hi=None):
    """
     [lo, hi)  is the search interval
    """
    if hi is None: hi = len(A)
    INF = float("inf")
    N = len(A)
    while lo < hi:
        mid = (lo+hi)//2
        left = A[mid-1] if mid > 0 else INF
        right = A[mid+1] if mid < N-1 else INF
        if A[mid] < left and A[mid] < right: return A[mid]
        if A[mid] > left:
            hi = mid
        else:
            lo = mid+1
    return INF

##

def local_minimum_ndim(A):
    """
    A is numpy ndim array
    """
    import numpy as np
    INF = float("inf")

    def neighbours(pos, shape):
        for i,(t,N) in enumerate(zip(pos,shape)):
            if t>0: yield pos[:i] + (t-1,) + pos[i+1:]
            if t<N-1: yield pos[:i] + (t+1,) + pos[i+1:]

    def midpoint(bdds):
        return tuple( (p[0]+p[1])//2 for p in bdds )

    def quadrant_boundary(pos, bdds):
        mids = midpoint(bdds)
        next_pos = []
        for p,m, (l,u) in zip(pos, mids, bdds):
            if p<m: next_pos.append((l,m))
            else: next_pos.append((m,u))
        return tuple(next_pos)

    def relative_coordinates(abscoor, bdds):
        return tuple(p-max(l,0) for p,(l,u) in zip(abscoor,bdds))

    def absoluate_coordinates(relcoor, bdds):
        return tuple(p+max(l,0) for p,(l,u) in zip(relcoor,bdds))


    shape = A.shape
    N = len(shape)
    bdds = tuple( (-1,v) for v in shape )
    while any(p[0]+1<p[1] for p in bdds):
        print("Boundary:", bdds)
        Inx = tuple(slice(max(a,0),b+1,None) for a,b in bdds)
        M = A[Inx]
        print(M)
        mids = midpoint(bdds)
        print("Midpoint:", A[mids], mids)
        search = tuple( (p[0], m, p[1])  for p,m in zip(bdds,mids))
        print("Search hyperplane:")
        print(search)
        min_frame = (INF,(INF,)*N)
        for i,p in enumerate(search):
            valid = tuple(t-max(bdds[i][0],0) for t in p if t>=0 and t<shape[i])
            print("Valids:")
            print(i,valid)
            T = M.take(valid, axis=i)
            print("Checking hyperplanes:")
            print(T)
            index = np.argmin(T)
            plane_pos = np.unravel_index(index, T.shape)
            val = T[plane_pos]
            mpos = plane_pos[:i] + (valid[ plane_pos[i] ],) + plane_pos[i+1:]
            pos = absoluate_coordinates(mpos, bdds)
            print(val, mpos, pos)
            min_frame = min(min_frame, (val,pos))
        
        print("Frame Best:",min_frame)
        v, pos = min_frame
        print("Neighbours:", list(neighbours(pos,shape)))
        for near in neighbours(pos, shape):
            if A[near] < v:
                print("Better:", A[near], near)
                bdds = quadrant_boundary(near, bdds)
                break
        else: return v, pos

    return None





##
