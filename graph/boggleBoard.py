class Trie:
    def __init__(self):
        self.root = {}
        self.isEnd = False

    def add(self, word):
        current = self.root
        for letters in word:
            if letters not in current:
                
