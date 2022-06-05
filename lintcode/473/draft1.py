class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False;
        self.word = None;


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        return self.dfs(self.trie.root, word, 0)

    def dfs(self, root, word, i):
        if word is None or root is None:
            return False;

        if i >= len(word):
            return root.is_word
        c = word[i]
        if c != '.':
            return self.dfs(root.children[c], word, i + 1)

        for node in root.children:
            if self.dfs(root.children[node], word, i + 1): return True

        return False;
