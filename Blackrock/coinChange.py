def coinChange(coins, amount):
    dp = [-1] * (amount + 1)

    # Base case for amount = 0, no coin necessary:
    dp[0] = 0
    for n in range(1, amount + 1):
        min_coins = float("inf")
        for c in coins:
            if c <= n and dp[n - c] != -1:
                cand = 1 + dp[n - c]
                min_coins = min(min_coins, cand)
                dp[n] = min_coins


    if dp[amount] == -1: return []

    b = amount
    sol = []
    while b > 0:
        for coin in coins:
            if coin <= b and dp[b] - 1 == dp[b - coin]:
                b -= coin
                sol.append(coin)
                break


    return (sol, dp[amount])



l = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50]
l2 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
l3 = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print(coinChange(l3, 4125))

