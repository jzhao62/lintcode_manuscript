class UnionFind:

    def __init__(self, n):
        self.orders = [-1 for i in range(n)]
        self.rank = [0 for i in range(n)]
        # count stands for number of connected part
        self.count = 0

    def setOrders(self, i):
        self.orders[i] = i
        self.count += 1

    def isValid(self, i):
        return self.orders[i] >= 0

    def find(self, i):
        # here use recursive way to update the orders.
        if self.orders[i] != i:
            self.orders[i] = self.find(self.orders[i])
        return self.orders[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)

        if x != y:
            if self.rank[x] > self.rank[y]:
                self.orders[y] = self.orders[x]
            elif self.rank[x] < self.rank[y]:
                self.orders[x] = self.orders[y]
            else:
                self.orders[y] = self.orders[x]
                self.rank[x] += 1
            self.count -= 1
