class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for x in range(31):
            if 2**x == n:
                return True
        return False
        