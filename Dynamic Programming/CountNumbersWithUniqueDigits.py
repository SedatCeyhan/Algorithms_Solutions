def countNumbersWithUniqueDigits(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1: dp[1] = 10

    for i in range(2, n + 1):
        count = 9
        digit = 9
        decimal = i - 1
        while decimal > 0:
            count *= digit
            digit -= 1
            decimal -= 1

        dp[i] = dp[i - 1] + count


    return dp[n]

print(countNumbersWithUniqueDigits(3))
