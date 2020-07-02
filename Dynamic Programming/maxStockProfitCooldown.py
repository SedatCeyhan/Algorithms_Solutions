class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2: return 0

        dp = []
        for day in range(n):
            dp.append([0,0,0,0])

        dp[0] = [-prices[0], 0, -prices[0], 0]
        dp[1] = [-prices[1], -prices[0] + prices[1], max(-prices[0], -prices[1]), max(0, -prices[0] + prices[1])]

        max_profit = max(dp[0][1], dp[1][1])

        for day in range(2, n):
            if day == n - 1:
                dp[day][0] = 0
                dp[day][1] = dp[day - 1][2] + prices[day]
                if max_profit < dp[day][1]: max_profit = dp[day][1]
                break

            dp[day][0] = dp[day - 2][3] - prices[day]
            dp[day][1] = dp[day - 1][2] + prices[day]
            dp[day][2] = max(dp[day][0], dp[day - 1][2])
            dp[day][3] = max(dp[day][1], dp[day - 1][3])
            if max_profit < dp[day][1]: max_profit = dp[day][1]

        return max_profit

sol = Solution()
print(sol.maxProfit([4,2,1]))