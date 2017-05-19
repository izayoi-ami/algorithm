##
class ExtendArray(object):
    def __init__(self,A,low=None,high=None, N=None):
        if N is None: N = len(A)
        if high is None: high = len(A)
        if low is None: low = 0
        self.A = A
        self.N = N
        self.low = low
        self.high = high
        pass

    def __getitem__(self, k):
        if k < 0: return float("-inf")
        if k >= self.N: return float("inf")
        return self.A[k]

    def cut(self, cut):
        return [self[k//2] for k in (cut-1, cut)]
    
    def twice_median(self):
        low, high = self.low, self.high
        M = high+low
        p1, p2 = (M-1)//2, M//2
        return self[p1]+self[p2]

    def size(self):
        return self.high - self.low

    def normal_size(self):
        return min(self.high, self.N) - max(self.low, 0)

    def remove_left(self, cnts=1):
        self.low+=cnts

    def remove_right(self, cnts=1):
        self.high-=cnts
    
    def elements(self):
        for i in xrange(self.low, self.high):
            yield self[i]

    def normal_elements(self):
        for i in xrange(max(self.low, 0), min(self.high, self.N)):
            yield self[i]

    def __repr__(self):
        return ":".join([repr(list(self.elements())),"({},{})".format(self.low,self.high)])

        

class Solution(object):
    test_cases = { 
        "case0":{
            "case":([1,3],[2]),
            "ans": 2.0,
        },
        "case1":{
            "case":([1,2],[3,4]),
            "ans": 2.5,
        },
        "case2":{
            "case":([1,1,1,1,3,4],[1,2,5]),
            "ans": 1.0,
        },
        "case3":{
            "case":([1],[2,3,4]),
            "ans": 2.5,
        },
        "case4":{
            "case":([1],[2,3,4,5]),
            "ans": 3.0,
        },
        "case5":{
            "case":([],[1,2,3,4]),
            "ans": 2.5,
        },
        "case6":{
            "case":([],[1,2,3,4,5]),
            "ans": 3.0,
        },
        "case7":{
            "case":([1,5],[2,3,4,6]),
            "ans": 3.5
        },
    }

    def __init__(self):
        self.solution = self.findMedianSortedArrays

    def answer(self, nums1, nums2):
        return ExtendArray(nums1+nums2).twice_median()/2.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
         
        n1, n2 = len(nums1), len(nums2)
        if n1<n2:
            n1, n2 = n2, n1
            nums1, nums2 = nums2, nums1
        if n2==0: return (nums1[(n1-1)//2] + nums1[n1//2])/2.0
        A = ExtendArray(nums1,-1,n1+1)
        B = ExtendArray(nums2,-1,n2+1)
        lo, hi = 0, 2*n2
        print(A, B, n1, n2)
        while lo<=hi:
            cut2 = (lo+hi)//2
            cut1 = n1+n2-cut2
            p1, p2 = A.cut(cut1), B.cut(cut2)
            if p1[0] > p2[1]: lo = cut2+1
            elif p2[0] > p1[1]: hi = cut2-1
            else: return (max(p1[0],p2[0])+min(p1[1],p2[1]))/2.0


        return None
    
##
