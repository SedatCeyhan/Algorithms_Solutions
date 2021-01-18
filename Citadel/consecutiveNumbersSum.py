import math

def consecutiveNumbersSum(N):
    count = 0
    # x > 0 --> N/k - (k + 1)/2 > 0
    upper_limit = math.ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
    for k in range(1, upper_limit):
        # x should be integer
        if (N - k * (k + 1) // 2) % k == 0:
            count += 1
    return count