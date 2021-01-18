def dieSimulator(n, rollMax):
    dp = []
    for i in range(n + 1):
        dp.append([0] * 7)

    for i in range(6):
        dp[1][i] = 1

    dp[0][6] = 1
    dp[1][6] = 6

    for r in range(2, n + 1):
        total = 0
        for d in range(6):
            if r - rollMax[d] <= 0:
                dp[r][d] = dp[r - 1][6]

            else:
                dp[r][d] = dp[r - 1][6] - (dp[r - rollMax[d] - 1][6] - dp[r - rollMax[d] - 1][d])

            total += dp[r][d]

        dp[r][6] = total

    return dp[n][6] % ((10 ** 9) + 7)




print(dieSimulator(2, [1,2,1,2,1,2]))