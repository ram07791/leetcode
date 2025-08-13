class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map ={}

        for i in nums:
            map[i] =map.get(i,0) +1
        
        for key in map:
            if map[key] >1:
                return True
        return False
        