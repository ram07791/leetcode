class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []

        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:  
                    prevRow = i - 1
                    leftVal = triangle[prevRow][j - 1]
                    rightVal = triangle[prevRow][j]
                    row.append(leftVal + rightVal)  
            triangle.append(row)

        return triangle[rowIndex]
        