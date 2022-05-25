from typing import (
    List,
)


class Solution:

    def social_network(self, n: int, a: List[int], b: List[int]) -> str:

        uf = UnionFind()
        m = len(a)

        for i in range(1, n + 1):
            uf.add(i)

        for i in range(m):
            uf.merge(a[i], b[i])

        return 'yes' if uf.connected_components_cnt == 1 else 'no'


class UnionFind:

    def __init__(self):
        self.father = {}
        self.connected_components_cnt = 0

    def add(self, x):
        if x in self.father: return
        self.father[x] = x
        self.connected_components_cnt += 1

    def find(self, x):
        if x == self.father[x]: return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return;

        self.father[x] = y
        self.connected_components_cnt -= 1
