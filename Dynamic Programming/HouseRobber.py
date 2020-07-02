def rob(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    F = []
    for i in range(n + 1):
        F.append([0,0])

    F[1] = [nums[0], 0]
    F[2] = [nums[0], nums[1]]

    for i in range(3, n + 1):
        if i != n:
            F[i][0] = max(nums[i-1] + F[i-2][0], F[i - 1][0])
            F[i][1] = max(nums[i-1] + F[i-2][1], F[i - 1][1])
        else:
            F[i][0] = max(nums[i - 1] + F[i - 2][0] - nums[0], F[i - 1][0])
            F[i][1] = max(nums[i - 1] + F[i - 2][1], F[i - 1][1])


    return max(F[n][0], F[n][1])

print(rob([1,2,3,1]))