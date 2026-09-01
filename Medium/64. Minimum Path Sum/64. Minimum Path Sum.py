# https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dp = [float('inf')] * cols
        dp[0] = 0

        for row in range(rows):
            for col in range(cols):

                if col > 0:
                    dp[col] = min(dp[col - 1], dp[col]) + grid[row][col]

                else:
                    dp[col] = dp[col] + grid[row][col]

        return dp[-1]



# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         rows = len(grid)
#         cols = len(grid[0])
#         dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
#         dp[0][0] = grid[0][0]

#         for row in range(rows):
#             for col in range(cols):

#                 if row > 0:
#                     dp[row][col] = dp[row - 1][col] + grid[row][col]

#                 if col > 0:
#                     dp[row][col] = min(dp[row][col], dp[row][col - 1] + grid[row][col])

#         return dp[-1][-1]