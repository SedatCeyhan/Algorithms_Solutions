def twoSum(nums, target):
    sumDict = {}
    for i in range(len(nums)):
        if target - nums[i] in sumDict:
            return [sumDict[target - nums[i]], i]
        else: sumDict[nums[i]] = i
