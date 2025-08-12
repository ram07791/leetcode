class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        T=[[1]]
        for i in range(rowIndex):
            t=[1]
            for k in range(len(T)-1):
                t.append(T[i][k]+T[i][k+1])
            t.append(1)
            T.append(t)
        return T[len(T)-1]
        