import math

def splitArray(val):
    n = len(val)
    if n == 0: return 0
    end_idx = n - 1
    splits = 0
    while end_idx >= 0:
        for l in range(end_idx + 1):
            if math.gcd(val[l], val[end_idx]) > 1:
                splits += 1
                end_idx = l - 1
                break

    return splits


print(splitArray([2,3,15,2,3,3]))
