def maxProfit(prices):
    n = len(prices)
    if n <= 1: return 0
    dp = [[-prices[0], 0], [max(-prices[0], -prices[1]), max(0, -prices[0] + prices[1])]]
    for day in range(2, n):
        curr_buy = max(dp[-2][1] - prices[day], dp[-1][0])
        curr_sell = max(dp[-1][0] + prices[day], dp[-1][1])
        dp.append([curr_buy, curr_sell])

    return dp[-1][1]





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