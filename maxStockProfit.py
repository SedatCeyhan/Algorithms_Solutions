def maximumProfit(price):
    # Write your code here

    n = len(price)
    if n < 2: return 0

    profit = 0
    max_price = 0
    max_day = 0
    day = 0
    while day < n - 1:
        for i in range(day, len(price)):
            if max_price <= price[i]:
                max_price = price[i]
                max_day = i
        buy_idx, sell_idx = day, max_day
        for day in range(buy_idx, sell_idx):
            profit -= price[day]

        profit += (sell_idx - buy_idx) * price[sell_idx]

        day = max_day + 1
        max_price = 0

    return profit


print(maximumProfit([19,3,15,2,17,6,4,2]))
