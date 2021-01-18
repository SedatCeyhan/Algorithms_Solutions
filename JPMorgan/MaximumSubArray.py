def maxSubArray(nums):
    if not nums: return 0
    n = len(nums)
    largest = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0: nums[i] += nums[i - 1]
        if largest < nums[i]: largest = nums[i]

    return largest

print(maxSubArray([-2]))


