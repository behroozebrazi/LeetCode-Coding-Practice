# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        totalProfit = 0
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):

            if prices[i - 1] > prices[i]:
                buy = prices[i]
                totalProfit += profit
                profit = 0
            else:
                profit = max(profit, prices[i] - buy)

        return totalProfit + profit