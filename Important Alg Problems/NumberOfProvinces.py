# Problem: https://leetcode.com/problems/number-of-provinces/
from collections import defaultdict

class Solution():
    def findCircleNum(self, M):
        n = len(M)
        discovered = defaultdict(lambda : False)
        count = 0

        def dfs(city):
            discovered[city] = True
            for c in range(n):
                if M[city][c] == 1 and not discovered[c]:
                    dfs(c)

        for c in range(n):
            if not discovered[c]:
                dfs(c)
                count+=1

        return count
