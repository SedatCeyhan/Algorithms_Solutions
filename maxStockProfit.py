# This is code contributed by SHUBHAMSINGH10


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximumProfit' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY price as parameter.
# #
#
# def maximumProfit(price):
#     # Write your code here
#
#     n = len(price)
#
#     # Cannot buy and sell if there is only 1 price (or not price at all)
#     if n < 2:
#         return 0
#
#     profit = 0
#
#     # (n - 1) is the last price and no reason to buy that one since we won't be able to sell it
#     i = 0
#     while i < n - 1:
#
#         # Find a local minimum to buy the stock
#         while i < n - 1:
#             if price[i + 1] <= price[i]:
#                 i += 1
#             else: break
#
#         # buy_idx has the smallest price in the sublist, namely local minimum
#         buy_idx = i
#
#         # No reason to bay last day's stock as we cannot sell it later
#         if buy_idx == n - 1: break
#
#         # Find a local maximum to sell the stock, we idx can be last stock price, since we're selling not buying
#         i += 1
#         while i <= n - 1:
#             if i == n - 1: break
#
#             if price[i] <= price[i + 1]:
#                 i += 1
#
#             else: break
#
#         # sell_idx has the greatest price in the sublist, namely local maximum
#         sell_idx = i
#
#         for day in range(buy_idx, sell_idx):
#             profit -= price[day]
#
#         profit += (sell_idx - buy_idx) * price[sell_idx]
#
#
#     return profit
#
# print(maximumProfit([3,2,5,3,5,2]))
#


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
