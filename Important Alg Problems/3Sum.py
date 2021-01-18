'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

'''

from collections import defaultdict
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3: return []

        nums = sorted(nums)

        sol = []
        discovered = defaultdict(lambda: False)
        for i in range(n):
            sum = -nums[i]
            L, R = i + 1, n - 1
            while L < R:
                if nums[L] + nums[R] == sum:
                    cand = [nums[i], nums[L], nums[R]]
                    if not discovered[tuple(cand)]:
                        discovered[tuple(cand)] = True
                        sol.append(cand)
                    L += 1
                    R -= 1

                elif nums[L] + nums[R] < sum: L += 1
                else: R -= 1

        return sol

    def twoSum(self, nums, target):
        n = len(nums)
        if n < 2: return []
        sol = []
        sumDict, discovered = {}, defaultdict(lambda: False)

        for i in range(n):
            if (target - nums[i]) in sumDict:
                cand = [target - nums[i], nums[i]]
                if not discovered[tuple(sorted(cand))]:
                    discovered[tuple(sorted(cand))] = True
                    sol.append(cand)
            sumDict[nums[i]] = i

        return sol








sol = Solution()
print(sol.twoSum([-1,0,1,2,-1,4], 3))


