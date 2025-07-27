class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        j=0
        n=len(nums)
        for i in range (1,n-1):
            if (nums[j] < nums[i]> nums[i+1]) or (nums[j] > nums[i] < nums[i+1]):
                count+=1
                j=i
        return count

        