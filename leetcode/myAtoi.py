##
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MIN = -2147483648
        MAX = 2147483647
        p = 0
        N = len(str)
        while p<N and str[p]==" ": p+=1
        if p==N: return 0
        sgn = 1
        if str[p] == "-": 
            sgn = -1
            p += 1
        elif str[p] == "+":
            sgn = 1
            p += 1
        tmp = 0
        p2 = p
        while p2 < N:
            c = str[p2]
            if c < "0" or c > "9": break
            val = ord(c)-ord("0")
            tmp = 10*tmp + val
            p2 += 1
        res = tmp * sgn
        if res < MIN: return MIN
        if res > MAX: return MAX
        return res


##
