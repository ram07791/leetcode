class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        cnt = 0
        prime = [1] *(n)
        if n>1:
            prime[0] = prime[1] = 0
        for i in range(2,int(n**0.5)+1):
            if prime[i] ==1:
                for j in range(i*i,n,i):
                    prime[j] = 0
        for i in prime:
            if i ==1:
                cnt+=1
        return cnt
        