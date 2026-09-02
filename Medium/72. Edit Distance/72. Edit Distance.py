# https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # first row and first column are numbered, and the rest are zero
        dp = [[i for i in range(n + 1)]]
        for i in range(1, m + 1):
            dp.append([i] + [0] * n)

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(
                        dp[i][j - 1],       # insert
                        dp[i - 1][j],       # delete
                        dp[i - 1][j - 1]    # replace
                    ) + 1

                else:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]