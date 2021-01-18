# THANK YOU!!! It was a really fun interview :)
def stock_runs(prices):
    n = len(prices)
    if n == 0: return 0

    # Dynamic Programming
    # dp[i] holds two integers: dp[i][0] <=> length of the longest increasing continuous subarray ending at prices[i]
    #                           dp[i][1] <=> length of the longest decreasing continuous subarray ending at prices[i]
    dp = []
    for i in range(n):
        # Trivially, each array item is by itself increasing/decreasing subarray,
        # so put 1 to both dp[i][0] and dp[i][1]
        dp.append([1, 1])

    longest = 1
    for i in range(1, n):
        # if the curr value is strictly greater than prev value,
        # then the length of longest increasing continuous subarray at prices[i] <=> 1 + dp[i - 1][0]
        if prices[i] > prices[i - 1]:
            dp[i][0] += dp[i - 1][0]

        # if the curr value is strictly less than prev value,
        # then the length of longest decreasing continuous subarray at prices[i] <=> 1 + dp[i - 1][1]
        elif prices[i] < prices[i - 1]:
            dp[i][1] += dp[i - 1][1]

        longest = max(longest, dp[i][0], dp[i][1])

    return longest


print(stock_runs([1,2,3]))
