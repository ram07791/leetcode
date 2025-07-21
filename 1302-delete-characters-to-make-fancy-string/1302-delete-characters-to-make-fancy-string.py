class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s[0]
        last = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] != last:
                last = s[i]
                count = 0

            count += 1
            if count > 2:
                continue

            result += s[i]

        return result
        