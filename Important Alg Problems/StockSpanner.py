'''
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days
(starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6]
'''


class StockSpanner:

    def __init__(self):
        self.dp = []
        self.prices = []

    def next(self, price: int) -> int:
        if not self.dp:
            self.dp.append(1)
            self.prices.append(price)
            return 1

        total, i = 1, len(self.prices) - 1
        while self.prices[i] <= price:
            total += self.dp[i]
            i -= self.dp[i]
            if i < 0: break

        self.prices.append(price)
        self.dp.append(total)
        return total





# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
stock = [31, 41, 48, 59, 79]
for p in stock:
    print(obj.next(p))