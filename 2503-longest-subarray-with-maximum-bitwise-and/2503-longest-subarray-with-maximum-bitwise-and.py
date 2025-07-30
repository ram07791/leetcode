class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = max(nums)
        max_len=0
        length=0

        for num in nums:
            if num == maxs:
                 length +=1
                 max_len = max(max_len, length)
            else:
                length=0
        return max_len

            
        