class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.idx = idx

    def find_pattern(self, pattern):
        node = self.root
        for c in pattern:
            node = node.children.get(c)
            if node is None: return -1

        return node.idx


class Solution:

    def is_palindrome(self, word):
        return word == word[::-1]

    def palindrome_pairs(self, words):
        trie = Trie()

        output = []

        for i in range(len(words)):
            w = words[i]
            trie.insert(w, i)

        for idx in range(len(words)):
            w = words[idx]

            for j in range(len(w) + 1):
                left_part = w[:j]
                right_part = w[j:]

                p1 = trie.find_pattern(left_part)
                p2 = trie.find_pattern(right_part)
                if p1 != -1 and p1 != idx and self.is_palindrome(right_part):
                    output.append([p1, idx])
                if p2 != -1 and p2 != idx and self.is_palindrome(left_part):
                    output.append([idx, p2])

        return output




input = ["bat", "tab", "cat"]

output = Solution().palindrome_pairs(input)

print(output)
