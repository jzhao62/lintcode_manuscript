class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
num = 5

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, num):
        node = self.root
        for i in range(32)[::-1]:
            bit = (num >> i) & 1
            if bit == 1:
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero



trie = Trie()

trie.add(5)

print('GG')

