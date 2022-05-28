DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        self.parent = {}
        self.size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.parent[(i, j)] = (i, j)
                    self.size += 1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    for delta_x, delta_y in DIRECTIONS:
                        x_ = x + delta_x
                        y_ = y + delta_y
                        if self.is_inbound(grid, x_, y_) and grid[x_][y_]:
                            # it is guaranteed the these 2 points belong to the same group
                            self.union((x, y), (x_, y_))
        return self.size

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_a] = root_b
            self.size -= 1

    def find(self, point):
        path = []
        while point != self.parent[point]:
            path.append(point)
            point = self.parent[point]

        for p in path:
            self.parent[p] = point
        return point

    def is_inbound(self, grid, x_, y_):
        if x_ < 0 or x_ > len(grid) - 1: return False;
        if y_ < 0 or y_ > len(grid[0]) - 1: return False;
        return True


island = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]


cnt = Solution().numIslands(island)

print(cnt)