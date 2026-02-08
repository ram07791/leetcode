class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = True
        if(dividend >0 and divisor < 0):
            sign = False
        elif(dividend <0 and divisor > 0):
            sign = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while(n>=d):
            cnt = 0
            while (n>= (d<<(cnt+1))):
                cnt+=1
            ans += 1<<cnt
            n = n - (d<<cnt)
        return ans if sign else (-1*ans)
