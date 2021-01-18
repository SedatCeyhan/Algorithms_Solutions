# Count and print the number of (contiguous) subarrays where the product of
# all the elements in the subarray is less than k
def numSubarrayProductLessThanK(nums, k):
    n = len(nums)
    if n == 0 or k <= 1: return 0
    total = 0
    left, product = 0, 1
    for right in range(n):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1

        total += right - left + 1

    return total

print(numSubarrayProductLessThanK([1,2,3], 0))

