##
class Solution(object):

    def answer(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos = {}
        N = len(s)
        for i,v in enumerate(s):
            if v not in pos: pos[v] = []
            pos[v].append(i)
        
        for L in xrange(N,0,-1):
            for i in xrange(N-L+1):
                if self.isPalindrome(s[i:i+L]): return s[i:i+L]

    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        d=[[True]*(k+1) + [False]*(N-1-k) for k in xrange(N)]
        res = (0,0)
        for k in range(1,N):
            for i in range(N-k):
                d[i][i+k] = s[i]==s[i+k] and d[i+1][i+k-1]
                if d[i][i+k]: res = (i,i+k)

        return s[res[0]:res[1]+1]
                    

            


    def isPalindrome(self, s):
        for i in xrange(len(s)//2):
            if s[i] != s[-1-i]: return False
        return True
        
##        
