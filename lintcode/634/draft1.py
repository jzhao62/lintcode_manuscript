from typing import (
    List,
)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None;
        return node

    def get_words_with_prefix(self, word):
        node = self.find(word)
        return [] if node is None else node.word_list



class Solution:
    def word_squares(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        squares = []
        for word in words:
            self.search(trie, [word], squares)
        return squares

    def search(self, trie, path, output):
        n = len(path[0])
        idx = len(path)

        if idx == n:
            output.append(list(path))
            return;

        for row_idx in range(idx, n):
            prefix = "".join([path[i][row_idx] for i in range(idx)])
            if trie.find(prefix) is None:
                return;

        prefix = "".join([path[i][idx] for i in range(idx)])

        for w in trie.get_words_with_prefix(prefix):
            path.append(w)
            self.search(trie, path, output)
            path.pop()







words = ["area","lead","wall","lady","ball"]


output = Solution().word_squares(words)