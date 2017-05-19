##
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        start = 0
        end = 0
        res = 0
        counter = {}
        while start < N:
            while end < N:
                c = s[end]
                last = counter.get(c, -1)
                if last>=start: 
                    res = max(res, end - start)
                    start = counter[c] + 1
                    break
                else:
                    counter[c] = end
                    end += 1
            else:
                res = max(res, end - start)
                start = end
        return res

##
        
