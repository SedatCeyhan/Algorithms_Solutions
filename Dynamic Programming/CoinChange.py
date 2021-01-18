def coinChange(coins, amount):
    if not coins or amount == 0: return 0
    coins.sort()

    dp = [0] * (amount + 1)

    for b in range(1, amount + 1):
        min_coins = float("inf")
        for coin in coins:
            if coin > b: break
            if dp[b - coin] != -1:
                if (1 + dp[b - coin]) < min_coins:
                    min_coins = 1 + dp[b - coin]

        if min_coins == float("inf"): dp[b] = -1
        else: dp[b] = min_coins

    return dp[amount]


print(coinChange([1,2,5], 14))
