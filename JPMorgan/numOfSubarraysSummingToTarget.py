# Given a list of non-negative numbers and a target integer k, write a function to
# check if the array has a continuous subarray of size at least 2 that sums up
# to a multiple of k, that is, sums up to n*k where n is also an integer

def checkSubarraySum(nums, k):
    n, k = len(nums), abs(k)
    if n <= 1: return False

    if k == 0:
        for i in range(1, n):
            if nums[i] == 0 and nums[i - 1] == 0: return True

        return False

    modulo_dict, sum = {0:-1}, 0
    for i in range(n):
        sum += nums[i]
        remainder = sum % k
        if remainder in modulo_dict:
            if modulo_dict[remainder] + 2 <= i: return True
        else: modulo_dict[remainder] = i

    return False

#print(checkSubarraySum([1, 2, 2], 2))


def subarraySum(nums, target):
    if not nums: return False
    sums, sum = [0], 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - target in sums: return True
        sums.append(sum)

    return False



def findNumberOfSubarraysTarget(nums, target):
    if not nums: return 0
    sums_dict, sum, sol = {0:1}, 0, 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - target in sums_dict: sol += sums_dict[sum - target]

        if sum in sums_dict: sums_dict[sum] += 1
        else: sums_dict[sum] = 1
    return sol

print(findNumberOfSubarraysTarget([0,1,0], 1))