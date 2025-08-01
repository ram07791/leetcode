class Solution(object):
    def factorial(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def nCr(self, n, r):
        return self.factorial(n) // (self.factorial(r) * self.factorial(n - r))
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for n in range(numRows):
            row = []
            for r in range(n + 1):
                row.append(self.nCr(n, r))
            triangle.append(row)
        return triangle