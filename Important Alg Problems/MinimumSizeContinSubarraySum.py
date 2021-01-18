'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

'''
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums: return 0
        sum, left = 0, 0
        minLen = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                minLen = min(minLen, i - left + 1)
                sum -= nums[left]
                left += 1

        return minLen if minLen != float('inf') else 0