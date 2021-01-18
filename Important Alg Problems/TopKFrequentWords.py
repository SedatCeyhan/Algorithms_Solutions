#problem: https://leetcode.com/problems/top-k-frequent-words/submissions/

from collections import defaultdict

class Solution:
    def topKFrequent(self, words, k):
        freqDict = defaultdict(lambda: 0)
        for word in words: freqDict[word] += 1
        freqDict = sorted(sorted(freqDict.items(), key=lambda item:item[0]), key=lambda item:item[1], reverse=True)
        sol = []
        for i in range(k): sol.append(freqDict[i][0])
        return sol


sol = Solution()
print(sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))



