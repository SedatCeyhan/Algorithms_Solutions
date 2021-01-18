'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagramDict = defaultdict(list)
        for str in strs:
            anagramDict[tuple(sorted(str))].append(str)

        return list(anagramDict.values())


sol = Solution()
print(sol.groupAnagrams(["ddddddddddg","dgggggggggg"]))


