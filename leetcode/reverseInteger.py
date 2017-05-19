##
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        MAX = 2147483647
        MIN = -2147483648
        if x==0: return 0
        mag = abs(x)
        res = int(math.copysign(int(str(mag)[::-1]),x))
        if res>MAX or res<MIN: return 0
        return res
##      
