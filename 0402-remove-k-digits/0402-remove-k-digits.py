class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st = []
        n= len(num)
        for i in range(n):
            while st and k>0 and st[-1] > num[i]:
                st.pop()
                k = k-1
            st.append(num[i])
        while(k>0):
            st.pop()
            k = k-1
        if not st:
            return "0"
        res = ""
        while(st):
            res = res + st.pop()
        res = res.rstrip("0")
        res = res[::-1]
        if not res:
            return "0"
        return res