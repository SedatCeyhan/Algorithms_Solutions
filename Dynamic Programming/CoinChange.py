def coinChange(coins, amount):
    # dp[i] = min # of coins to sum i
    dp = [0] * (amount + 1)

    for m in range(1, amount + 1):
        min_coin_count = float('inf')
        for coin in coins:
            if coin <= m:
                cand = 1 + dp[m - coin]
                if dp[m - coin] != -1 and cand < min_coin_count:
                    min_coin_count = cand

        if min_coin_count != float('inf'):
            dp[m] = min_coin_count
        else:
            dp[m] = -1

    return dp[amount]

print(coinChange([2], 11))


