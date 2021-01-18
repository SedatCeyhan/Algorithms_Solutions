from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0

        discovered, adjMap = defaultdict(lambda: False), defaultdict(list)
        L = len(beginWord)

        for word in wordList:
            for i in range(L):
                adjMap[word[:i] + "*" + word[i+1:]].append(word)

        discovered[beginWord] = True
        queue = [(beginWord, 1)]
        while queue:
            currWord, path = queue.pop(0)
            if currWord == endWord: return path
            for i in range(L):
                adjList = adjMap[currWord[:i] + "*" + currWord[i+1:]]
                for word in adjList:
                    if not discovered[word]:
                        discovered[word] = True
                        queue.append((word, path + 1))
        return 0




sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))