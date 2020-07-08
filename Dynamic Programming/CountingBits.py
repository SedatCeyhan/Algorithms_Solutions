def countBits(num):
    dp = [0] * (num + 1)
    one_bits = [0]

    degree = 0
    for m in range(1, num + 1):
        curr_factor = 2 ** degree
        dp[m] = 1 + dp[m - curr_factor]
        one_bits.append(dp[m])
        if (m + 1) == 2 ** (degree + 1):
            degree += 1

    return one_bits

print(countBits(0))