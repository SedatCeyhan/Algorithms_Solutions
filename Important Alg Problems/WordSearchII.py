'''
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

'''
from collections import defaultdict

class Solution:
    def findWords(self, board, words):
        if not board or not words: return []
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        sol = []

        rootNode = {}
        for word in words:
            currNode = rootNode
            for i in range(len(word)):
                if word[i] not in currNode:
                    currNode[word[i]] = {}
                currNode = currNode[word[i]]

            currNode["end"] = word

        def isValid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols and not self.discovered[(r,c)]


        def dfs_backtrack(r, c, node):
            self.discovered[(r,c)] = True
            node = node[board[r][c]]
            if "end" in node: sol.append(node['end'])
            for d in directions:
                nbr = (r + d[0], c + d[1])
                if isValid(nbr[0], nbr[1]) and board[nbr[0]][nbr[1]] in node:
                    dfs_backtrack(nbr[0], nbr[1], node)
                    self.discovered[(nbr[0], nbr[1])] = False


        for r in range(rows):
            for c in range(cols):
                self.discovered = defaultdict(lambda: False)
                currNode = rootNode
                char = board[r][c]
                if char in currNode:
                    dfs_backtrack(r, c, currNode)
                    self.discovered[(r,c)] = False

        return list(set(sol))



sol = Solution()
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','n','r'],
  ['i','f','i','a']
]

board2 = [
  ['a', 'a']
]
#words = ["oath","pea","eat","peach","rat","rain"]
words = ["a"]
print(sol.findWords(board2, words))
