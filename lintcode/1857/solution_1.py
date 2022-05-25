from typing import (
    List,
)


class Solution:
    """
    @param M: a matrix of integer
    @return: return an Integer
    """

    def findCircleNum(self, M):
        # write your code here
        n = len(M)
        uf = UF()
        for i in range(n):
            uf.add(i)

        for j in range(n):
            for i in range(j):
                if M[i][j] == 1:
                    uf.merge(i, j)

        return uf.parts


class UF:
    def __init__(self):
        self.father = {}
        self.parts = 0

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.parts += 1

    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        self.father[root_x] = root_y
        self.parts -= 1


x = 2

print(~x)