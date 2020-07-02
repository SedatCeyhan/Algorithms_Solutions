def nthUglyNumber(n):
    dp = []

    # 1 is the first ugly number
    dp.append(1)

    i2, i3, i5 = 0, 0, 0
    while len(dp) < n:
        next_ugly = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
        dp.append(next_ugly)

        if next_ugly == dp[i2] * 2:
            i2+=1
        if next_ugly == dp[i3] * 3:
            i3+=1
        if next_ugly == dp[i5] * 5:
            i5+=1

    return dp[-1]

print(nthUglyNumber(7))
