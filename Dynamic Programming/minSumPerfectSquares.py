import math

def numSquares(n):
    squares = []
    for i in range(1, int(math.sqrt(n)) + 1):
        squares.append(i ** 2)

    dp = [0] * (n + 1)

    for m in range(1, n + 1):
        minCount = float('inf')
        for square in squares:
            if square > m: break
            cand = 1 + dp[m - square]
            if cand < minCount:
                minCount = cand
        dp[m] = minCount


    return dp[n]

print(numSquares(113))