from collections import defaultdict

'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

'''
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList: return []
        discovered, genericDict, L = defaultdict(lambda: False), defaultdict(list), len(beginWord)
        wordToMinPath = defaultdict(lambda: -1)
        minPath, sol = float('inf'), []

        for word in wordList:
            for i in range(L):
                genericDict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = [(beginWord, 0, [])]
        while queue:
            word, path, words = queue.pop(0)
            path += 1
            newList = words + [word]
            for i in range(L):
                hasFound = False
                for w in genericDict[word[:i] + "*" + word[i + 1:]]:
                    if w == endWord:
                        if minPath < path: return sol
                        else:
                            minPath = path
                            hasFound = True
                            sol.append(newList + [w])
                            break

                    elif not discovered[w] or wordToMinPath[w] == path:
                        discovered[w] = True
                        wordToMinPath[w] = path
                        queue.append((w, path, newList))

                if hasFound: break

        return sol

sol = Solution()
print(sol.findLadders('hit','cog', ["hot","dit","dot","dog","lot","log","cog"]))