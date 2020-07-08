def integerBreak(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for m in range(2, n + 1):
        max_product = 0
        for i in range(1, m):
            cand = max(i * dp[m - i], i * (m - i))
            if cand > max_product:
                max_product = cand

        dp[m] = max_product

    return dp[n]

print(integerBreak(10))