class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node.children[c] = node.children.get(c, TrieNode())
            node = node.children[c]
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node


DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    def boggleGame(self, board, words):
        if not board or not board[0]:
            return 0
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.paths = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, set([(i, j)]), trie.find(board[i][j]))
        res = 0
        for path in self.paths:
            coords = path.copy()
            count = 1
            for neighbor in self.paths:
                if neighbor.isdisjoint(coords):
                    coords.update(neighbor.copy())
                    count += 1
            res = max(res, count)

        return res

    def dfs(self, i, j, board, path, node):
        if node is None:
            return
        if node.is_word:
            self.paths.append(path.copy())

        for dx, dy in DIRECTIONS:
            x, y = i + dx, j + dy
            if not self.is_valid(x, y, board) or (x,y) in path:
                continue
            path.add((x, y))
            self.dfs(x, y, board, path, node.children.get(board[x][y]))
            path.remove((x, y))

    def is_valid(self, i, j, board):
        if i < 0 or i > len(board)-1: return False;
        if j < 0 or j > len(board[0])-1: return False
        return True




board = ["abc","def","ghi"]
words = ["abc","defi","gh"]



output = Solution().boggleGame(board, words)

print(output)