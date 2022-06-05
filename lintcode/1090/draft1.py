class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None;
        self.val = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, val):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.val = val
        node.word = word

    def find_last(self, prefix):
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if node is None:
                return None

        return node


class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key, val):
        self.trie.insert(key, val)

    def sum(self, prefix):
        node_to_start = self.trie.find_last(prefix)
        result = []

        self.dfs(node_to_start, result)

        output = 0

        for v in result:
            output += v

        return output

    def dfs(self, node, result):
        if node is None:
            return

        if node.is_word:
            result.append(node.val)

        for node in node.children:
            self.dfs(node.children[node], result)


s = MapSum()
s.insert("apple", 3)
s.sum("ap")
s.insert("app", 2)
s.sum("ap")
