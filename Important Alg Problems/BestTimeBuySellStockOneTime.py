class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        minPrice, maxProfit = float('inf'), 0

        for day in range(n):
            if prices[day] < minPrice: minPrice = prices[day]
            else: maxProfit = max(maxProfit, prices[day] - minPrice)

        return maxProfit
