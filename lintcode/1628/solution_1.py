from typing import (
    List,
)


class Solution:

    def drivingProblem(self, L, W, p):
        p.append((-1, 0))
        p.append((-1, W))
        n = len(p)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                x0, y0 = p[i]
                x1, y1 = p[j]

        # 如果是在路边，dist allowed = 5 (车的直径+一个路墩子的半径)
                if x0 == -1 or x1 == -1:
                    dist = abs(y1 - y0)
                    if dist <= 5:
                        uf.union(i, j)
         # dist allowed = 6 两个路墩子的半径 + 车的直径
                else:
                    dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
                    if dist <= 6:
                        uf.union(i, j)

        return 'no' if uf.cnt == 1 else 'yes'
        # 这种写法也可以
        # return "no" if uf.find(n - 2) == uf.find(n - 1) else "yes"


class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.cnt = n

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.father[rootA] = rootB
            self.cnt -= 1