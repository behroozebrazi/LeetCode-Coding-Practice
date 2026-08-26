# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, cols)
            # row = mid // cols
            # col = mid % cols

            if target < matrix[row][col]:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True

        return False