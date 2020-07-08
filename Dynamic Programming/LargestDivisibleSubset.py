def largestDivisibleSubset(nums):
    n = len(nums)
    if n <= 1: return nums

    nums = list(sorted(nums))

    dp = []
    for num in nums:
        dp.append([num])


    max_subset = [nums[0]]
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if nums[i] % dp[j][-1] == 0:
                if len(dp[i]) < len(dp[j] + [nums[i]]):
                    dp[i] = dp[j] + [nums[i]]
                if len(dp[i]) > len(max_subset):
                    max_subset = dp[i]


    return max_subset


print(largestDivisibleSubset([4,8,10,240]))