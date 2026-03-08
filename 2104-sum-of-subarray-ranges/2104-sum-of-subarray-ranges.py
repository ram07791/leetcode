class Solution(object):
    def find_nse(self,nums):
        n = len(nums)
        st = []
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while(st and nums[st[-1]] >= nums[i]):
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans
    def find_psee(self,nums):
        n = len(nums)
        st = []
        ans = [0] * n
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans
    def find_nge(self,nums):
        n = len(nums)
        st = []
        ans = [0] * n  
        for i in range(n-1,-1,-1):
            while(st and nums[st[-1]] <= nums[i]):
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans
    def find_pgee(self,nums):
        n = len(nums)
        st = []
        ans = [0] * n  
        for i in range(n):
            while(st and nums[st[-1]] < nums[i]):
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans
    def subArrayMin(self,nums):
        nse = self.find_nse(nums)
        psee = self.find_psee(nums)
        n =len(nums)
        total = 0
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            freq = (left * right * 1)
            val = (freq * nums[i])
            total = (total + val) 
        return total
    def subArrayMax(self,nums):
        nge = self.find_nge(nums)
        pgee = self.find_pgee(nums)
        n = len(nums)
        total = 0
        for i in range(n):
            left = i - pgee[i]
            right = nge[i] - i
            freq = (left * right * 1)
            val = (freq * nums[i])
            total = (total + val) 
        return total
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (self.subArrayMax(nums) - self.subArrayMin(nums))