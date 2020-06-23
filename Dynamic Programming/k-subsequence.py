def kSub(k, nums):

    n = len(nums)
    k_remainders = []
    for i in range(k + 1):
        k_remainders.append(0)

    sum = 0
    for i in range(n):
        sum += nums[i]
        k_remainders[sum % k] += 1

    count = 0
    for i in range(k):
        if k_remainders[i] > 1:
            count += (k_remainders[i] * (k_remainders[i] - 1)) // 2

    count += k_remainders[0]
    return count


print(kSub(5, [5,10,11,9,5]))