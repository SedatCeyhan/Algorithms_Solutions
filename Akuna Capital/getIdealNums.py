def getIdealNums(l, r):
    dp = []

    # 1 is the first ideal number
    dp.append(1)
    next_ideal = 1
    count = 0

    i3, i5 = 0, 0
    while next_ideal <= r:
        if next_ideal >= l: count += 1

        next_ideal = min(dp[i3] * 3, dp[i5] * 5)
        dp.append(next_ideal)

        if next_ideal == dp[i3] * 3:
            i3 += 1
        if next_ideal == dp[i5] * 5:
            i5 += 1

    print(dp)
    return count


print(getIdealNums(1, 225))