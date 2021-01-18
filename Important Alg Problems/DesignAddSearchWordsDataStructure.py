# Question: https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        curr = self.trie
        for i in range(len(word)):
            char = word[i]
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['END'] = word


    def search(self, word):
        curr = self.trie
        currDicts = [curr]
        for i in range(len(word)):
            if currDicts:
                char = word[i]
                temp = []
                if char == '.':
                    for node in currDicts:
                        if type(node) == dict:
                            temp.extend(list(node.values()))
                    currDicts = temp
                else:
                    for node in currDicts:
                        if type(node) == dict:
                            if char in node:
                                temp.append(node[char])
                    currDicts = temp

        for node in currDicts:
            if 'END' in node:
                return True
        return False

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("mad")
wd.addWord("pad")
print(wd.search('b..'))
