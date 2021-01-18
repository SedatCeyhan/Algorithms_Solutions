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




class Solution(object):
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        if n <= 1: return nums

        nums.sort()
        nums[0] = [nums[0]]

        max_count, max_subset = 1, nums[0]
        for i in range(1, n):
            local, sbst = 1, []
            for j in range(i):
                if nums[i] % nums[j][-1] == 0 and len(nums[j]) + 1 > local:
                    local = len(nums[j]) + 1
                    sbst = nums[j]

            nums[i] = sbst + [nums[i]]
            if max_count < local:
                max_count = local
                max_subset = nums[i]

        return max_subset




print(Solution().largestDivisibleSubset([4,8,10,240]))