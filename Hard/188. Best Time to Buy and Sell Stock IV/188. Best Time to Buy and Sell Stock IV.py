# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        days = len(prices)
        # dp[t][i] = maximum profit at transaction t, from day 0 through day i
        dp = [ [0] * days for _ in range(k + 1) ]

        for t in range(1, k + 1):
            buy_price = float("inf")

            for i in range(days):

                # effective cost at the same day = buy price - profit from previous transaction
                buy_price = min(prices[i] - dp[t - 1][i], buy_price)

                # maximum profit so far
                dp[t][i] = max(prices[i] - buy_price, dp[t][i - 1])

        return dp[-1][-1]