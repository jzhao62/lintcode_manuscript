steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:

    def numIslands(self, grid) -> int:

        h = len(grid)
        w = len(grid[0])

        self.visited = [[False] * w for _ in range(h)]

        output = 0;

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    output += 1
                    self.dfs(grid, i, j)

        return output

    def dfs(self, grid, x, y):
        if not self.isValid(x, y, grid):
            return
        self.visited[x][y] = True
        
        print(x, y, self.visited)

        for dx, dy in steps:
            self.dfs(grid, x + dx, y + dy)

    def isValid(self, x, y, grid):
        if not (0 <= x and x < len(grid)): return False;
        if not (0 <= y and y < len(grid[0])): return False;

        if self.visited[x][y]:
            return False;

        return True


s = Solution()

grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
output = s.numIslands(grid)

print(output)
