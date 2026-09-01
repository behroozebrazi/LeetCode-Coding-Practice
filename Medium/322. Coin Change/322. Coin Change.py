# https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        amount += 1
        dp = [amount] * amount
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != amount else -1