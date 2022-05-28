from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:

        uf = UnionFind()

        output = []

        for operator in operators:
            x, y = operator.x, operator.y
            if (x, y) in uf.island:
                output.append(uf.connected_components_cnt)
                continue;

            uf.add((x, y))

            for dx, dy in DIRECTIONS:
                x_ = x + dx
                y_ = y + dy
                if (x_, y_) in uf.island:
                    uf.merge((x_, y_), (x, y))

            output.append(uf.connected_components_cnt)

        return output


class UnionFind:

    def __init__(self):
        self.father = {}
        self.island = set()
        self.connected_components_cnt = 0

    def add(self, x):
        if x in self.father: return
        self.father[x] = x
        self.island.add(x)
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