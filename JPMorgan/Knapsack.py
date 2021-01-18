def knapsack(weights, profits, limit):
    n = len(weights)
    # Dynamic programming array: dp[m][w] holds the max profit with contraint limit = w formed by a subset from weights[1:m]
    # we're interested in dp[n][limit]
    dp = [[0] * (limit + 1) for m in range(n + 1)]

    #Recursive part:
    for w in range(1, limit + 1):
        for m in range(1, n + 1):
            if w < weights[m - 1]: dp[m][w] = dp[m - 1][w]
            else: dp[m][w] = max(dp[m-1][w], profits[m - 1] + dp[m - 1][w - weights[m - 1]])



    # At this point dp[n][limit] holds the max profit formed by a subset from weights[1:n] with a limit weight = limit
    # Recovery step to find that maximizing subset
    sol, profit, m, w = [], dp[n][limit], n, limit
    while profit > 0:
        if dp[m][w] == dp[m - 1][w]:
            m -= 1
        else:
            profit -= profits[m - 1]
            sol.append([weights[m - 1], profits[m - 1]])
            m -= 1
            w -= weights[m - 1]

    return sorted(sol, key=lambda item:item[0])



#print(knapsack([5, 4, 6, 3], [10, 40, 30, 50], 10))

pr = [100, 180, 260, 310, 40, 535, 695]

def stockTrial(prices):
    n = len(prices)
    if n < 2: return 0
    prices[0] = [-prices[0], 0]
    for d in range(1, n):
        prices[d] = [max(prices[d - 1][0], prices[d - 1][1] - prices[d]), max(prices[d - 1][1], prices[d - 1][0] + prices[d])]

    transactions, profit, d = [], prices[n - 1][1], n - 1
    while profit > 0:
        if profit == prices[d - 1][0] + pr[d]:
            transactions.insert(0, "SELL at DAY " + str(d))
            profit -= pr[d]
            d -= 1
        elif profit == prices[d - 1][1] - pr[d]:
            transactions.insert(0, "BUY at DAY " + str(d))
            profit += pr[d]
            d -= 1
        else: d-= 1

    if profit < 0: transactions.insert(0, "BUY at DAY " + str(pr.index(-profit)))
    return transactions



print(stockTrial([100, 180, 260, 310, 40, 535, 695]))







