from typing import (
    List,
)

from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    """
    @param a: a List[List[int]]
    @return: Return the maximum score of a path
    """

    def maximum_minimum_path(self, a: List[List[int]]) -> int:
        n, m = len(a), len(a[0])

        left, right = 0, min(a[n - 1][m - 1], a[0][0])

        def path_exists(val):
            visited = set()

            def dfs(cur_row, cur_col):
                if cur_row == n - 1 and cur_col == m - 1:
                    return True

                visited.add((cur_row, cur_col))
                for dx, dy in DIRECTIONS:
                    new_row = cur_row + dx
                    new_col = cur_col + dy

                    if self.is_valid(new_row, new_col, a, visited):
                        if a[new_row][new_col] >= val and dfs(new_row, new_col):
                            visited.remove((cur_row, cur_col))
                            return True
                visited.remove((cur_row, cur_col))
                return False

            return dfs(0, 0)

        while left + 1 < right:
            mid = (left + right) // 2

            if path_exists(mid):
                left = mid;
            else:
                right = mid;

        if path_exists(right): return right;
        return left

    def is_valid(self, x, y, a, visited):
        if x < 0 or x > len(a) - 1: return False;
        if y < 0 or y > len(a[0]) - 1: return False;
        if (x, y) in visited: return False;
        return True;



input = [[5,4,5],[1,2,6],[7,4,6]]

output = Solution().maximum_minimum_path(input)

print(output)
