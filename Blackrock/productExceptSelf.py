def productExceptSelf(nums):
    n = len(nums)

    L, R = [1] * n, [1] * n

    for i in range(1, n):
        L[i] = L[i - 1] * nums[i - 1]
        j = n - i - 1
        R[j] = R[j + 1] * nums[j + 1]

    for i in range(n):
        nums[i] = L[i] * R[i]

    return nums



print(productExceptSelf([1, 2]))

