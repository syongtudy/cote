# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy_day in range(0, len(prices) - 1):
            for sell_day in range(buy_day + 1, len(prices)):
                if prices[sell_day] - prices[buy_day] > max_profit:
                    max_profit = prices[sell_day] - prices[buy_day]
        return max_profit