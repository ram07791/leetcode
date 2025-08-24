class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.strip().split()

        if not a:
            return 0
        else:
            return len(a[-1])

        