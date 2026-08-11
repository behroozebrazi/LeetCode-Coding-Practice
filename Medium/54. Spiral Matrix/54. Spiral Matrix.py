# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        rows = [0, len(matrix) - 1]
        cols = [0, len(matrix[0]) - 1]
        row = 0
        col = 0

        while True:

            row = rows[0]
            for col in range(cols[0], cols[1] + 1):
                result.append(matrix[row][col])
            rows[0] += 1

            col = cols[1]
            for row in range(rows[0], rows[1] + 1):
                result.append(matrix[row][col])
            cols[1] -= 1
            
            if rows[0] > rows[1] or cols[0] > cols[1]:
                break

            row = rows[1]
            for col in range(cols[1], cols[0] - 1, -1):
                result.append(matrix[row][col])
            rows[1] -= 1

            col = cols[0]
            for row in range(rows[1], rows[0] - 1, -1):
                result.append(matrix[row][col])
            cols[0] += 1

            if rows[0] > rows[1] or cols[0] > cols[1]:
                break

        return result