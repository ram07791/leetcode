class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for x in range(20):
            if 3**x == n:
                return True
           
        return False
              
        