from typing import (
    List,
)

DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c, None)
            if node is None:
                return None;

        return node


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        tree = TrieTree()
        tree.add(word)

        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                c = board[i][j]
                if self.dfs(board, tree.root.children.get(c), i, j, set([(i, j)])):
                    return True;

        return False;

    def dfs(self, board, node, x, y, visited):
        if node is None: return False;
        if node.is_word: return True;

        for dx, dy in DIRECTION:
            if not self.in_bound(board, x + dx, y + dy, visited): continue
            visited.add((x + dx, y + dy))
            if self.dfs(board, node.children.get(board[x + dx][y + dy]), x + dx, y + dy, visited):
                return True
            visited.remove((x + dx, y + dy))

    def in_bound(self, board, i, j, visited):
        if i < 0 or i > len(board) - 1: return False;
        if j < 0 or j > len(board[0]) - 1: return False;
        if (i, j) in visited: return False

        return True


board = ["ABCE", "SFCS", "ADEE"]
word = "ABCCED"
ret = Solution().exist(board, word)
