import  math

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

#print(integerBreak(10))


# def integerBreak2(n):
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1):
#         max_product = -float("inf")
#         for j in range(i - 1, int(math.ceil(i / 2)) - 1, -1):
#             cand = max(dp[j] * dp[i - j], dp[j] * (i - j), j * dp[i - j], j * (i - j))
#             if cand > max_product: max_product = cand
#
#         dp[i] = max_product
#
#     return dp[n]


import math

import math


class Solution(object):
    def integerBreak(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, ((int)(i / 2)) + 1):
                dp[i] = max(j * (i - j), (i - j) * dp[j], dp[i - j] * j, dp[i - j] * dp[j])

        return dp


sol = Solution()
print(sol.integerBreak(9))
