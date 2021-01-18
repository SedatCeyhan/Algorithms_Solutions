'''
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. T
wo combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

[2,3,5] -> 8   =====> [2,2,2,2], [2,3,3], [3,5]

'''

class Solution:
    def combinationSum(self, candidates, target):
        if not candidates: return []
        candidates = sorted(candidates)
        sol, comb = [], []
        self.hasExceeded = False

        def backtrack(start, sum):
            comb.append(candidates[start])
            sum += comb[-1]
            if sum == target:
                sol.append(list(comb))
                self.hasExceeded = True

            elif sum > target:
                self.hasExceeded = True
                return

            for i in range(start, len(candidates)):
                backtrack(i, sum)
                comb.pop()
                if self.hasExceeded:
                    self.hasExceeded = False
                    break


        for i in range(len(candidates)):
            backtrack(i, 0)
            comb.pop()
            if self.hasExceeded:
                self.hasExceeded = False
                break

        return sol

# sol = Solution()
# print(sol.combinationSum([2,3,5,8,9], 8))

class Solution_MoreCurrent:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        solSet = []
        self.hasExceeded = False

        def backtrack(cands, sum, start):
            if sum == target:
                solSet.append(list(cands))
                self.hasExceeded = True
                return
            elif sum > target:
                self.hasExceeded = True
                return

            for i in range(start, len(candidates)):
                cnds = cands + [candidates[i]]
                sum += candidates[i]
                backtrack(cnds, sum, i)
                sum -= candidates[i]
                if self.hasExceeded:
                    self.hasExceeded = False
                    return

        for i in range(len(candidates)):
            backtrack([candidates[i]], candidates[i], i)


        return solSet



sol2 = Solution_MoreCurrent()
print(len(sol2.combinationSum([3,5,7,8,9,10,11], 22)))
