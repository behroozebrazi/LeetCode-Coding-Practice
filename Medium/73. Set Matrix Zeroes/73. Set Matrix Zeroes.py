# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeroRows = set()
        zeroCols = set()
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroRows.add(row)
                    zeroCols.add(col)

        for row in zeroRows:
            for col in range(n):
                 matrix[row][col] = 0

        for col in zeroCols:
            for row in range(m):
                matrix[row][col] = 0