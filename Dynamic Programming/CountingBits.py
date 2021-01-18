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




def countBits2(num):
    if num == 0: return [0]
    dp = [0, 1]
    degree = 1
    for i in range(2, num + 1):
        if i < 2 ** degree:
            dp.append(1 + dp[i - (2 ** (degree - 1))])
        else:
            dp.append(1)
            degree += 1

    return dp



def countBitss(num):
    bits = [0]
    degree = 0
    for n in range(1, num + 1):
        if 2 ** degree == n:
            bits.append(1)
            degree += 1
        else:
            bits.append(1 + bits[n - (2 ** (degree - 1))])

    return bits


print(countBitss(2))
