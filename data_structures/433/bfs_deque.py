from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

        visited = set()

        output = 0;

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, visited, i, j)
                    output += 1

        return output

    def bfs(self, grid, visited, x, y):
        q = deque([(x, y)])
        visited.add((x, y))
        while q:
            x, y = q.popleft()
            for d_x, d_y in DIRECTIONS:
                if not self.is_valid(grid, x + d_x, y + d_y, visited):
                    continue;
                q.append((x + d_x, y + d_y))
                visited.add((x + d_x, y + d_y))

    def is_valid(self, grid, x, y, visited):

        if x < 0 or x > len(grid) - 1:
            return False;

        if y < 0 or y > len(grid[0]) - 1:
            return False;

        if (x, y) in visited:
            return False

        return grid[x][y]