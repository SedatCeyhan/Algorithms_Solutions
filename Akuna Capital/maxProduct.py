def maxProduct(nums):
    n = len(nums)
    if n == 0: return 0

    nums[0] = (nums[0], nums[0])
    sol = nums[0][0]

    for i in range(1, n):
        if nums[i] > 0:
            curr_min = min(nums[i], nums[i] * nums[i - 1][0])
            curr_max = max(nums[i], nums[i] * nums[i - 1][1])
        else:
            curr_min = min(nums[i], nums[i] * nums[i - 1][1])
            curr_max = max(nums[i], nums[i] * nums[i - 1][0])

        nums[i] = (curr_min, curr_max)
        if sol < curr_max: sol = curr_max

    return sol




print(maxProduct([1,2,-1,-2,2,1,-2,1,4,-5,4,0]))