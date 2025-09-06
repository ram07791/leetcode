class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        first=abs(z-x)
        sec=abs(z-y)
        if first==sec:
            return 0
        return 1 if first < sec else 2