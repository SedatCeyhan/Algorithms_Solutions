class Solution:
    def combinationSum(self, candidates, target):
        results = []
        candidates = sorted(candidates)
        def backtrack(start, comb, sum):
            if sum == target:
                results.append(list(comb))
                return
            elif sum > target:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, sum + candidates[i])
                comb.pop()


        backtrack(0, [], 0)
        return results

sol = Solution()
print(sol.combinationSum([2,3,7,6], 19))