

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None;
        self.is_word = False;

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode
            node = node.children[c]

        node.word = word
        node.is_word = True





class Solution:

    def find_all_concatenated_words_in_a_dict(self, words):

        trie = Trie()

        for w in words:
            trie.insert(w)

        self.root = trie.root

        output = []

        for w in words:
            if self.is_concatenated(self.root, w, 0) and w != "":
                output.append(w)

        return output





    def is_concatenated(self, node, word, idx):
        if idx == len(word):
            return node.is_word

        for c in node.children:
            # 如果当前分支无关，跳过
            if word[idx] != c: continue;

            if node.children[c].is_word and node.children[c].word == word: return False

            if node.children[c].is_word and self.is_concatenated(self.root, word, idx+1): return True;
            if self.is_concatenated(node.children[c], word, idx+1): return True;


        return False;



