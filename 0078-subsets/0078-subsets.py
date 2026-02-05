class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        power = pow(2,n)
        for num in range (power):
            subset =  []
            for i in range (n):
                if num & (1<<i):
                    subset.append(nums[i])
            res.append(subset)
        return res