class Solution(object):
    def find_nse(self,arr):
        n = len(arr)
        st = []
        ans = [0] * n
        for i in range(n-1,-1,-1):
            while(st and arr[st[-1]] >= arr[i]):
                st.pop()
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans
    def find_psee(self,arr):
        n = len(arr)
        st = []
        ans = [0] * n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nse = self.find_nse(arr)
        psee = self.find_psee(arr)
        n =len(arr)
        mod = int(1e9+7)
        total = 0
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            freq = (left * right * 1)
            val = (freq * arr[i]) % mod
            total = (total + val) % mod
        return total