# Question: https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount, coins):
        if amount == 0: return 1
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amnt in range(coin, amount + 1):
                dp[amnt] += dp[amnt - coin]

        return dp[amount]









sol = Solution()
print(sol.change(22,[3,5,7,8,9,10,11]))