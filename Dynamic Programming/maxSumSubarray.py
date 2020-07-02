def maxSumSubarray(nums):

    if len(nums) == 0: return 0

    n = len(nums)
    F = []

    for i in range(n + 1):
        F.append(0)

    max = nums[0]
    idx = 0
    for i in range(1, n + 1):
        curr = nums[i - 1]
        if F[i - 1] > 0:
            F[i] = curr + F[i - 1]
        else:
            F[i] = curr

        if max < F[i]:
            max = F[i]
            idx = i - 1

    sum = 0
    sol = []
    while sum != max:
       sol.insert(0, nums[idx])
       sum += nums[idx]
       idx -= 1

    return sol

print(maxSumSubarray([-2, 2, 3, -6, 5]))


