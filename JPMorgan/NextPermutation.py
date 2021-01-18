def nextPermutation(nums):
    map, stack = {}, []
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] < nums[stack[-1]]:
            map[stack.pop()] = i
        if map: break
        stack.append(i)

    if map:
        minimum = float("inf")
        for k in map:
            if nums[k] < minimum:
                minimum = nums[k]
                min_idx = k
        temp = nums[map[min_idx]]
        nums[map[min_idx]] = nums[min_idx]
        nums[min_idx] = temp

        l = nums[map[min_idx] + 1:]
        l.sort()
        nums[map[min_idx] + 1:] = l
    else:
        nums.sort()

    return nums


print(nextPermutation([1,3,2]))

