def maxProfit(prices):
    min_day = 0
    profit = 0
    day = 1
    while day < len(prices) - 1:
        if prices[day] < prices[min_day]:
            min_day = day
            day += 1
        elif prices[day] > prices[day - 1] and prices[day] > prices[day + 1]:
            profit += prices[day] - prices[min_day]
            min_day = day + 1
            day += 2
        else:day += 1

    n = len(prices)
    if prices[n - 1] > prices[n - 2] and prices[n - 1] > prices[min_day]: profit += prices[n - 1] - prices[min_day]
    return profit



print(maxProfit([5,2,3,2,6,6,2,9,1,0,7,4,5,0]))