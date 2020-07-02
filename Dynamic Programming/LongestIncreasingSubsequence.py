def lengthOfLIS(nums):
    n = len(nums)
    if n == 0: return 0

    dp = [0] * (n + 1)

    max_length1 = 0
    for i in range(1, n + 1):
        max_length2 = 0
        for j in range(1, i):
            if nums[j - 1] < nums[i - 1] and max_length2 < dp[j]:
                max_length2 = dp[j]

        dp[i] = max_length2 + 1
        if max_length1 < dp[i]: max_length1 = dp[i]

    return max_length1


print(lengthOfLIS([]))

