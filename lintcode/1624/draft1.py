class TrieNode:
    def __init__(self):
        self.is_end = False
        self.height = 1
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for i, c in enumerate(s):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.height = max(node.height, len(s) - i)
        node.is_end = True


class Solution:
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def get_ans(self, str_list):
        trie = Trie()
        for s in str_list:
            trie.insert(s)

        return self.calc_diff(trie.root)

    def calc_diff(self, node):
        diff = 0
        if len(node.children) == 2:
            diff = max(diff, node.children['0'].height + node.children['1'].height)
        for c in node.children:
            diff = max(diff, self.calc_diff(node.children[c]))
        if len(node.children) == 1 and node.is_end:
            diff = max(diff, node.height - 1)
        return diff



words = ["01","0","0101010"]



x = Solution().get_ans(words)

print(x)


