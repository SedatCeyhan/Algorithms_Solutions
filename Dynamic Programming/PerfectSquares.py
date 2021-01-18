import math

def numSquares(n):
    if n == 0: return 0
    squares = []

    for i in range(1, int(math.sqrt(n)) + 1):
        squares.append(i ** 2)

    dp = [0] * (n + 1)

    for m in range(1, n + 1):
        min_count_squares = float('inf')
        for square in squares:
            if square <= m:
                cand = 1 + dp[m - square]
                if cand < min_count_squares:
                    min_count_squares = cand

        dp[m] = min_count_squares

    return dp[n]

print(numSquares(19))