class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 +nums2
        merged.sort()

        n= len(merged)

        if n % 2 ==1:
            return float(merged[n // 2])
        else:
            middle1=merged[n // 2 - 1]
            middle2 = merged[n // 2]
            return (float(middle1) + float(middle2)) / 2.0