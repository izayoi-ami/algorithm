##
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        tmp = zip(nums,range(len(nums)))
        tmp.sort()
        print(tmp)
        for i,(v,pos) in enumerate(tmp):
            try:
                t = (target-v,-1)
                p = bisect.bisect_left(tmp,t, lo=i+1)
                w, pos2 = tmp[p]
                if v+w == target:
                    if pos<pos2: return [pos,pos2]
                    return [pos2,pos]
            except IndexError:
                pass


##      
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = {}
        for i,v in enumerate(nums):
            try: return [i,pos[target-v]]
            except KeyError: pos[v] = i

##
