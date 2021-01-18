def minPrice(cost):
    dp = []
    for block in cost:
        dp.append([0] * 3)
    dp[0] = cost[0]
    for b in range(1, len(cost)):
        dp[b][0] = cost[b][0] + min(dp[b - 1][1], dp[b - 1][2])
        dp[b][1] = cost[b][1] + min(dp[b - 1][0], dp[b - 1][2])
        dp[b][2] = cost[b][2] + min(dp[b - 1][0], dp[b - 1][1])

    return min(dp[-1])

print(minPrice([[1,2,2], [2,2,1], [2,1,2]]))