class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        lmax , rmax , total = 0,0,0
        l = 0
        r = n-1
        while(l<r):
            if(height[l] <= height[r]):
                if lmax > height[l]:
                    total+=lmax - height[l]
                else:
                    lmax =height[l]
                l+=1
            else:
                if rmax > height[r] :
                    total+=rmax-height[r]
                else:
                    rmax = height[r]
                r-=1
        return total
