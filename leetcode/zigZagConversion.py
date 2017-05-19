##
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        from itertools import izip_longest, chain
        if numRows == 1: return s
        N = 2*(numRows-1)
        res = s[::N]
        for k in range(1,numRows-1):
            res += "".join(chain(*izip_longest(s[k::N],s[N-k::N],fillvalue="")))
        res += s[numRows-1::N]
        return res
##
