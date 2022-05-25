from typing import (
    List,
)

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:

    def find_circle_num(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        total_cnt = 0

        for j in range(n):
            for i in range(j):
                if grid[i][j] == 1:
                    total_cnt += 1
                    self.dfs(grid, i, j)
                    print(grid)

        return total_cnt

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        for dx, dy in DIRECTIONS:
            if self.is_valid(grid, i + dx, j + dy):
                self.dfs(grid, i + dx, j + dy)

    def is_valid(self, grid, i, j):
        if i < 0 or i > len(grid) - 1: return False;
        if j < 0 or j > len(grid[0]) - 1: return False;
        return grid[i][j] == 1




grid = [[1,0,0,0,0],[0,1,0,0,1],[0,0,1,0,0],[0,0,0,1,0],[0,1,0,0,1]]
output = Solution().find_circle_num(grid)

print(output)