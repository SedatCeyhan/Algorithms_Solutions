'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

'''
from collections import defaultdict

class Solution:
    def findCircleNum(self, M):
        if not M: return 0
        circles = 0
        friendDict, discovered = defaultdict(list), defaultdict(lambda: False)
        N = len(M)

        def dfs(n):
            discovered[n] = True
            for f in range(N):
                if n != f and M[n][f] == 1 and not discovered[f]:
                    dfs(f)

        for r in range(N):
            if not discovered[r]:
                for c in range(N):
                    if M[r][c] == 1 and not discovered[c]:
                        dfs(c)
                        circles += 1


        return circles


sol = Solution()
print(sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))



