class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIdx(self, char):
        return ord(char) - ord('a')


    def insert(self, word):
        currNode = self.root
        for level in range(len(word)):
            if not currNode.children[self.charToIdx(word[level])]:
                currNode.children[self.charToIdx(word[level])] = TrieNode()
            currNode = currNode.children[self.charToIdx(word[level])]

        currNode.isLeaf = True


    def search(self, word):
        currNode = self.root
        for level in range(len(word)):
            if not currNode.children[self.charToIdx(word[level])]: return False
            currNode = currNode.children[self.charToIdx(word[level])]

        return currNode.isLeaf



    def startsWith(self, prefix):
        currNode = self.root
        for level in range(len(prefix)):
            if not currNode.children[self.charToIdx(prefix[level])]: return False
            currNode = currNode.children[self.charToIdx(prefix[level])]

        return True












# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)