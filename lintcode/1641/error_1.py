class Solution:

    def get_ans(self, mp) -> int:
        uf = UnionFind()

        n, m = len(mp), len(mp[0])
        horizontal, vertical = {}, {}

        for i in range(n):
            for j in range(m):
                if mp[i][j] == 1:
                    uf.add((i, j))
                    horizontal[i] = (i, j)
                    vertical[j] = (i, j)

        for i in range(n):
            for j in range(m):
                if mp[i][j] == 1:
                    uf.merge((i, j), horizontal[i])
                    uf.merge((i, j), vertical[j])

        return uf.merge_cnt


class UnionFind:
    def __init__(self):
        self.father = {}
        self.merge_cnt = 0

    def add(self, x):
        if x in self.father: return
        self.father[x] = x

    def find(self, x):
        if self.father[x] == x: return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return
        self.father[x] = y
        self.merge_cnt += 1


mp = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 0]]

cnt = Solution().get_ans(mp)

print(cnt)
