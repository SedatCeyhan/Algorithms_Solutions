import math

# find all the square summable numbers between 1,..., n
def squareSummable(n):
    squares = []
    for i in range(1, int(math.sqrt(n)) + 1):
        squares.append(i ** 2)

    dp = []
    for m in range(len(squares) + 1):
        dp.append([0] * (n + 1))
        dp[m][0] = 1

    square_summables = []
    for b in range(1, n + 1):
        for m in range(1, len(squares) + 1):
            if b < squares[m - 1]:
                dp[m][b] = dp[m - 1][b]
            else:
                dp[m][b] = max(dp[m - 1][b], dp[m - 1][b - squares[m - 1]])

        if dp[len(squares)][b] == 1:
            square_summables.append(b)


    return len(square_summables)


print(squareSummable(20))


# Find the n'th integer that is a square summable
def squareSummable_nth(n):
    squares = []
    for i in range(1, int(math.sqrt(n)) + 1):
        squares.append(i ** 2)

    dp = []
    for m in range(len(squares) + 1):
        dp.append([0] * (n + 1))
        dp[m][0] = 1

    square_summables = []
    for b in range(1, n + 1):
        for m in range(1, len(squares) + 1):
            if b < squares[m - 1]:
                dp[m][b] = dp[m - 1][b]
            else:
                dp[m][b] = max(dp[m - 1][b], dp[m - 1][b - squares[m - 1]])

        if dp[len(squares)][b] == 1:
            square_summables.append(b)


    return square_summables