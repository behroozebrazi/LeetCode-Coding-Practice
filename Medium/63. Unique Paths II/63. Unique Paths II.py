# https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[0] = 1

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]

        return dp[-1]



# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

#         rows = len(obstacleGrid)
#         cols = len(obstacleGrid[0])
#         dp = [[0 for _ in range(cols)] for _ in range(rows)]
#         if obstacleGrid[0][0] == 0:
#             dp[0][0] = 1

#         for row in range(rows):
#             for col in range(cols):
#                 if obstacleGrid[row][col] == 0:
#                     if row > 0:
#                         dp[row][col] += dp[row - 1][col]
#                     if col > 0:
#                         dp[row][col] += dp[row][col - 1]

#         return dp[-1][-1]