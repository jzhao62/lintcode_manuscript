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
                node.children[c] = TrieNode()
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

            # 如果当前node.children中包含了完整的 word，说明它肯定不是concatenated word
            if node.children[c].is_word and node.children[c].word == word: return False

            # 如果 0-> idx 是word，并且idx+1 -> end 出现在其他分支中，并且是concatenated word，那么它的组合必然是concatenated word

            if node.children[c].is_word and self.is_concatenated(self.root, word, idx + 1): return True;
            # 如果 0-> idx 是word，并且idx+1 -> end 出现在接下来的分支，并且是concatenated word，那么它的组合必然是concatenated word

            if self.is_concatenated(node.children[c], word, idx + 1): return True;

        return False;


words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

output = Solution().find_all_concatenated_words_in_a_dict(words)

print(output)
