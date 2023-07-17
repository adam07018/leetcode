class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range (len(string)):
            node = self.root
            for j in range (i, len(string)):
                letter = string[j]
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node[self.endSymbol] = {}

    def contains(self, string):
        node = self.root
        for i in range (len(string)):
            if string[i] not in node:
                return False
            node = node[string[i]]
        if self.endSymbol not in node:
            return False
        return True

trie = SuffixTrie('babc')
print(trie.contains('bc'))