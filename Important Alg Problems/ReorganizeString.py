'''

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

aab -> aba
aaab -> ""

'''

from collections import defaultdict
import math
class Solution:
    def reorganizeString(self, S):
        n = len(S)
        if n <= 1: return S

        maxFreq = 0
        freqDict = defaultdict(lambda: 0)
        for c in S:
            freqDict[c] += 1
            maxFreq = max(maxFreq, freqDict[c])

        others = n - maxFreq
        if maxFreq - others > 1: return ""

        freqDict = sorted(freqDict.items(), key=lambda item:item[1], reverse=True)
        chars = []
        for c in freqDict:
            chars.extend(c[0] * c[1])


        sol = [0] * n
        sol[::2], sol[1::2] = chars[:(int)(math.ceil(n/2))], chars[(int)(math.ceil(n/2)):]
        return "".join(sol)






sol = Solution()
#print(sol.reorganizeString("aab"))
#print(sol.reorganizeString("eqmeyggvp"))
print(sol.reorganizeString("abbabbaaab"))



