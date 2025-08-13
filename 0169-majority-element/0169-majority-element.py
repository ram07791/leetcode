class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map={}

        for i in nums:
            map[i] = map.get(i,0) +1
        
        for key in map:
            if map[key] > len(nums)//2:
                return key
        return -1
       

        