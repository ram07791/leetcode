class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d= {')':'(', ']' : '[', '}':'{'}
        stack=[]
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or stack[-1] != d[i] :
                    return False
                stack.pop()
        return not stack