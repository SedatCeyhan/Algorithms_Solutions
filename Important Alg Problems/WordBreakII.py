from collections import defaultdict
from collections import Counter

class Solution:
    def wordBreak(self, s, wordDict):
        if not s or not wordDict: return []
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True
        indices = []

        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                curr = s[j-1:i] in wordDict and dp[j - 1]
                dp[i] = dp[i] or curr
                if curr: indices.append([j, i])

        if not dp[n]: return []

        indices = sorted(sorted(indices, key=lambda item:item[1]), key=lambda item:item[0])
        sol = []
        map = defaultdict(list)
        stack = []

        for i in range(len(indices)):
            if indices[i][0] == 1: stack.append([(indices[i][0], indices[i][1]), ""])
            for j in range(i + 1, len(indices)):
                if indices[j][0] == indices[i][1] + 1:
                    map[(indices[i][0], indices[i][1])].append((indices[j][0], indices[j][1]))

        while stack:
            word, sent = stack.pop()
            sent += s[word[0] - 1: word[1]] + " "
            if map[word]:
                for word in map[word]:
                    stack.append([word, sent])
            elif word[1] == n:
                sol.append(sent[:-1])


        return sol




# sol = Solution()
# # print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
# print(sol.wordBreak("abcd", ['a', 'abc', 'b', 'cd']))
class Solution2:
    def wordBreak(self, s, wordDict):
        if not s or not wordDict or (set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys())): return []
        n = len(s)
        dp = [[]] * (n + 1)
        dp[0] = [""]

        wordDict = set(wordDict)
        for endIdx in range(1, n + 1):
            sublist = []
            for startIdx in range(1, endIdx + 1):
                if s[startIdx - 1: endIdx] in wordDict:
                    for subSentence in dp[startIdx - 1]:
                        sublist.append(str(subSentence + " " + s[startIdx - 1: endIdx]).strip())

            dp[endIdx] = sublist

        return dp[n]

sol = Solution2()
print(sol.wordBreak("catsandog", ["cat", "cats", "and", "sand", "dog"]))