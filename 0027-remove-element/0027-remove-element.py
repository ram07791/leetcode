class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        x=0
        for i in range(n):
            if(nums[i]!=val):
                nums[x] = nums[i]
                x=x+1
        return x
        