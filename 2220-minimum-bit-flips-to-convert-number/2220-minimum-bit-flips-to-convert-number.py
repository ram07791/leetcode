class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ans = start ^ goal
        cnt = 0
        while ans !=0:
            ans = ans & ans-1
            cnt+=1
        return cnt
        