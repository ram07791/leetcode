class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        for q,t in sorted(((x,'ab'),(y,'ba')))[::-1]:
            stack = []
            for ch in s:
                if stack and stack[-1]+ch == t:
                    res += q
                    stack.pop()
                else:
                    stack.append(ch)
        
            s = stack

        return res
       
        