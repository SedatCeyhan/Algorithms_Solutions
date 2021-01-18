def maxProfit(prices):
    n = len(prices)
    if n == 0: return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)

    return max_profit





def maxProfit_Multiple(prices):
    n = len(prices)
    if n <= 1: return 0
    dp = [[-prices[0], 0], [max(-prices[0], -prices[1]), max(0, -prices[0] + prices[1])]]
    for day in range(2, n):
        curr_buy = max(dp[-2][1] - prices[day], dp[-1][0])
        curr_sell = max(dp[-1][0] + prices[day], dp[-1][1])
        dp.append([curr_buy, curr_sell])

    return dp[-1][1]

pr = [100, 180, 260, 310, 40, 535, 695]

# def stockTrial(prices):
#     n = len(prices)
#     if n < 2: return 0
#     prices[0] = [-prices[0], 0]
#     for d in range(1, n):
#         prices[d] = [max(prices[d - 1][0], prices[d - 1][1] - prices[d]), max(prices[d - 1][1], prices[d - 1][0] + prices[d])]
#
#     transactions, profit, d = [], prices[n - 1][1], n - 1
#     while profit > 0:
#         if profit == prices[d - 1][0] + pr[d]:
#             transactions.insert(0, "SELL at DAY " + str(d))
#             profit -= pr[d]
#             d -= 1
#         elif profit == prices[d - 1][1] - pr[d]:
#             transactions.insert(0, "BUY at DAY " + str(d))
#             profit += pr[d]
#             d -= 1
#         else: d-= 1
#
#     if profit < 0: transactions.insert(0, "BUY at DAY " + str(pr.index(-profit)))
#     return transactions
#
#
#
# print(stockTrial([100, 180, 260, 310, 40, 535, 695]))
#





def maxProfit_NO_Cooldown(prices):
    n = len(prices)
    if n < 2: return 0
    dp = [[-prices[0], 0], [max(-prices[0], -prices[1]), max(0, prices[1] - prices[0])]]
    for day in range(2, n):
        curr_buy = max(dp[-1][0], -prices[day] + dp[-1][1])
        curr_sell = max(dp[-1][1], prices[day] + dp[-1][0])
        dp.append([curr_buy, curr_sell])

    return dp[-1][1]


print(maxProfit_NO_Cooldown([100, 180, 260, 310, 40, 535, 695]))

