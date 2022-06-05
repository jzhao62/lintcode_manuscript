REVERSE_KEYBOARD = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "x": "9", "y": "9", "z": "9",
}


class TrieNode:

    def __init__(self):
        self.word_count = 0
        self.children = {}

    def add(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_count += 1


class Solution:

    def letterCombinationsII(self, queries, dict):

        mapped_words = []

        for pattern in dict:
            w = []
            for c in pattern:
                w.append(REVERSE_KEYBOARD[c])

            mapped_words.append("".join(w))

        root = TrieNode()
        output = []
        for word in mapped_words:
            root.add(word)

        for q in queries:
            node = root

            for c in q:
                if c not in node.children:
                    node = None;
                    break;
                node = node.children[c]

            output.append(node.word_count if node is not None else 0)

        return output

Input = ["2", "3", "4"]
dict = ["a","abc","de","fg"]


output = Solution().letterCombinationsII(Input, dict)

print(output)