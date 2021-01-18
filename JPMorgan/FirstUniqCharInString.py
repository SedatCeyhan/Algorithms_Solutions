def firstUniqChar(s):
    map = {}
    for c in s:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    for c in map:
        if map[c] == 1: return s.index(c)

    return -1

print(firstUniqChar("dddccdbba"))


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1