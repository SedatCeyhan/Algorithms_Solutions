def search(nums, target):
    n = len(nums)
    start, end = 0, n - 1
    while start <= end:
        m = int((start + end)/2)
        if target == nums[m]: return m
        elif nums[start] <= nums[m]:
            if nums[start] <= target < nums[m]:
                end = m - 1
            else:
                start = m + 1
        else:
            if nums[m] < target <= nums[end]:
                start = m + 1
            else:
                end = m - 1

    return -1



print(search([4,5,6,7,0,2], 5))