# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        # dp[t][i] = maximum profit at transaction t, from day 0 through day i
        dp = [[0] * n for _ in range(3)]

        for t in range(1, 3):
            buy_price = float("inf")

            for i in range(n):

                # effective cost = buy price - profit from previous transaction
                buy_price = min(buy_price, prices[i] - dp[t - 1][i])

                # maximum profit so far
                dp[t][i] = max(dp[t][i - 1], prices[i] - buy_price)

        return dp[2][-1]



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         profit1 = 0
#         profit2 = 0

#         buy_price1 = float("inf")
#         buy_price2 = float("inf")

#         for price in prices:

#             # First transaction
#             buy_price1 = min(buy_price1, price)
#             profit1 = max(profit1, price - buy_price1)

#             # Second transaction
#             buy_price2 = min(buy_price2, price - profit1)
#             profit2 = max(profit2, price - buy_price2)

#         return profit2