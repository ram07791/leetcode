class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result= nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left= i+1
            right = len(nums)-1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if abs(target - total) < abs(target - result):
                    result = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result

            
        