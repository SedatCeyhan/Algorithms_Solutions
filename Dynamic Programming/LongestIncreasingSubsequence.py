# def lengthOfLIS(nums):
#     n = len(nums)
#     if n == 0: return 0
#
#     dp = [0] * (n + 1)
#
#     max_length1 = 0
#     for i in range(1, n + 1):
#         max_length2 = 0
#         for j in range(1, i):
#             if nums[j - 1] < nums[i - 1] and max_length2 < dp[j]:
#                 max_length2 = dp[j]
#
#         dp[i] = max_length2 + 1
#         if max_length1 < dp[i]: max_length1 = dp[i]
#
#     return max_length1
#
#
# print(lengthOfLIS([5,4,3,6,4,7]))
#
# def LongestIncreasingSubarray(nums):
#     n = len(nums)
#     if n == 0: return 0
#     dp = [1] * (n + 1)
#     dp[0] = 0
#     max_length = 1
#     for i in range(2, n + 1):
#         if nums[i - 1] > nums[i - 2]:
#             dp[i] = 1 + dp[i - 1]
#             if max_length < dp[i]: max_length = dp[i]
#
#     return max_length
#
#
# print(LongestIncreasingSubarray([5, 4, 3, 6, 4, 7]))
#

def LIS1(nums):
    if len(nums) <= 1: return len(nums)
    n = len(nums)
    dp = [1] * (n + 1)
    dp[0] = 0

    longest = 1
    for i in range(2, n + 1):
        local_longest = 1
        for j in range(1, i):
            if nums[j - 1] < nums[i - 1]:
                local_longest = max(local_longest, 1 + dp[j])
        dp[i] = local_longest
        if dp[i] > longest: longest = dp[i]

    return longest


print(LIS1([2, 4, 3, 6, 7, 7]))



def LIS2(nums):
    if len(nums) <= 1: return len(nums)
    n = len(nums)
    dp = [1] * (n + 1)
    dp[0] = 0

    longest = 1
    for i in range(2, n + 1):
        if nums[i - 2] < nums[i - 1]:
            dp[i] = 1 + dp[i - 1]
            if longest < dp[i]: longest = dp[i]

    return longest

print(LIS2([3, 4, 7,12]))