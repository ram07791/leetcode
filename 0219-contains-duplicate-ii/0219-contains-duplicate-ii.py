class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        lookup = {}
        
        for i in range(len(nums)):
            
            
            if nums[i] in lookup and abs(lookup[nums[i]]-i) <= k:
                return True
            
           
            lookup[nums[i]] = i
        
        return False  
           
        