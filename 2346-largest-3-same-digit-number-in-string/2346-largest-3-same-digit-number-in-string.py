class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        for d in "9876543210":
            triple = d * 3
            if triple in num:
                return triple
        return ""
        