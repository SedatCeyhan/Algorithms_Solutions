def missingNumber(nums):
    missing = 0
    nums = sorted(nums)
    for n in nums:
        if missing < n: return missing
        missing += 1

    return nums[-1] + 1

l = [1, 16, 3, 2]
print(set(l))


