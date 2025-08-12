class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans=""
        for c in s:
            if c.isalnum():
                letter=c.lower()
                ans=ans+letter
        
        i=0
        j=len(ans)-1
        while(i<j):
            if(ans[i]!=ans[j]):
                
                return False
            else:
                j=j-1
                i=i+1
        return True
        