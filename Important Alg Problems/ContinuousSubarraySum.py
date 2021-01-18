'''
Given a list of non-negative numbers and a target integer k, write a function to check
if the array has a continuous subarray of size at least 2 that sums up to a multiple of k,
that is, sums up to n*k where n is also an integer.
'''

from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2: return 0
        k = abs(k)

        if k == 0:
            for i in range(1, len(nums)):
                if nums[i-1] == 0 and nums[i] == 0: return True
            return False

        mod = 0
        moduloDict = {0:-1}
        for i in range(len(nums)):
            mod = (mod + nums[i]) % k
            if mod in moduloDict:
                if i - moduloDict[mod] >= 2: return [moduloDict[mod] + 1, i]
            else: moduloDict[mod] = i

        return False

    # How many of those?
    def checkSubarraySumCount(self, nums, k):
        if len(nums) < 2: return 0
        k = abs(k)

        indexPairs = []
        sum, count = 0, 0
        moduloToIdx = defaultdict(list)
        moduloToIdx[0] = [-1]
        for i in range(len(nums)):
            sum += nums[i]
            mod = sum % k
            if mod in moduloToIdx:
                for idx in moduloToIdx[mod]:
                    if i - idx >= 2:
                        count += 1
                        indexPairs.append([idx + 1, i])

            moduloToIdx[mod].append(i)

        return indexPairs




sol = Solution()
#print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))
print(sol.checkSubarraySumCount([23, 2, 6, 4, 7], 6))

