class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for x in range(30):
            if 4**x == n:
                return True
        return False
        