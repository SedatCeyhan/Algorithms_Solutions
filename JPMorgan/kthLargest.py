def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))