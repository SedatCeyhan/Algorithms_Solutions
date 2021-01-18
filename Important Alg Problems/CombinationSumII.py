'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
'''

from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        self.numCount, self.currNumCount = defaultdict(lambda: 0), defaultdict(lambda: 0)
        self.hasExceeded = False
        solSet = []
        for i in range(len(candidates)):
            self.numCount[candidates[i]] += 1
        candidates = list(set(candidates))


        def backtrack(cands, sum, start):
            if sum == target:
                solSet.append(cands)
                self.hasExceeded = True
                return

            elif sum > target:
                self.hasExceeded = True
                return

            for i in range(start, len(candidates)):
                if self.currNumCount[candidates[i]] < self.numCount[candidates[i]]:
                    cnds = cands + [candidates[i]]
                    self.currNumCount[candidates[i]] += 1
                    sum += candidates[i]
                    backtrack(cnds, sum, i)
                    sum -= candidates[i]
                    self.currNumCount[candidates[i]] -= 1
                    if self.hasExceeded:
                        self.hasExceeded = False
                        return

        for i in range(len(candidates)):
            self.currNumCount[candidates[i]] = 1
            backtrack([candidates[i]], candidates[i], i)
            self.currNumCount[candidates[i]] = 0

        return solSet




sol = Solution()
print(sol.combinationSum2([2,5,2,1,2],5))
#print(sol.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))