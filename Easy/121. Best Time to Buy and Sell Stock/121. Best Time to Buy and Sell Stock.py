# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = prices[0]

        for price in prices:

            buy = min(buy, price)

            profit = max(profit, price - buy)

        return profit