class Solution:
    def minimum_length_encoding(self, words):
        trie = Trie()
        for w in words:
            trie.insert_word("".join(list(reversed(w))))
        return self.dfs(trie.root)

    def dfs(self, node):
        if not node.children or node.is_word:
            return len(node.word) + 1

        cnt = 0

        for c in node.children:
            cnt += self.dfs(node.children[c])
        return cnt


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root

        for c in word:
            if c not in node:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True
        node.word = word
