from typing import (
    List,
)




class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.prefix_cnt = 0



class Trie:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
                node = node.children[c]
            node.prefix_cnt +=1

        node.is_word = True




class Solution:
    def short_perfix(self, string_array: List[str]) -> List[str]:
        trie = Trie()
        root = trie.get_root();
        output = []

        for w in string_array:
            trie.insert(w)

        for w in string_array:
            output.append(self.get_unique_prefix(w, root))

        return output



    def get_unique_prefix(self, word, root):
        node = root
        for i in range(len(word)):
            if node.prefix_cnt == 1:
                return word[:i]
            node = node.children[word[i]]

        return word
