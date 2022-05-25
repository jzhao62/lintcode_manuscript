class Solution:


    def __init__(self):
        self.father = {}
        self.cnt = 0

    def add(self, x):
        if x in self.father: return
        self.father[x] = x

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.father[x] = y

        # 这里的cnt 记录merge了多少次（有多少次 1 -> 0)
        self.cnt +=1

    def get_ans(self, mp):

        line, column, m, n = {}, {}, len(mp), len(mp[0])
        for i in range(m):
            for j in range(n):
                if mp[i][j]:
                    self.add((i, j))
                    line[i] = (i, j)
                    column[j] = (i, j)

        for i in range(m):
            for j in range(n):
                if mp[i][j]:
                    self.merge((i, j), line[i])
                    self.merge((i, j), column[j])

        return self.cnt


mp = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 0]]

cnt = Solution().get_ans(mp)

print(cnt)
