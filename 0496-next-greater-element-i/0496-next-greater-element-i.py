class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums2)
        st = []
        nge = [0] * n
        for j in range(n-1,-1,-1):
            while(st and st[-1] <= nums2[j]):
                st.pop()
            if( not st):
                nge[j] = -1
            else:
                nge[j] = st[-1]
            st.append(nums2[j])
        res=[]
        for num in nums1:
            idx = nums2.index(num)
            res.append(nge[idx])
        return res


        
            