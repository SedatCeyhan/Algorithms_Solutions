# Question: https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        freqDict = defaultdict(lambda: 0)
        for num in nums:
            freqDict[num] += 1

        freqDict = sorted(freqDict.items(), key=lambda item:item[1], reverse=True)
        sol = []
        for i in range(k):
            sol.append(freqDict[i][0])

        return sol
