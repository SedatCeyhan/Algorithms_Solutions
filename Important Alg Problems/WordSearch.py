'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
 where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

from collections import defaultdict
class Solution:
    def exist(self, board, word):
        if not board or not word: return False
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        discovered = defaultdict(lambda: False)

        def isValid(r, c, charIdx):
            return r >= 0 and r < rows and c >= 0 and c < cols and board[r][c] == word[charIdx]

        def dfs_backtrack(r, c, charIdx):
            if charIdx == len(word) - 1: return True
            discovered[(r,c)] = True
            for d in directions:
                nbr = (r + d[0], c + d[1])
                if isValid(nbr[0], nbr[1], charIdx + 1) and not discovered[(nbr[0], nbr[1])]:
                    if dfs_backtrack(nbr[0], nbr[1], charIdx + 1): return True
                    discovered[(nbr[0], nbr[1])] = False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs_backtrack(r, c, 0): return True
                    discovered[(r, c)] = False


        return False

sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ASADFBC"))