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


        # start -> end 的max value 由起点，终点的最小值决定，这也是一个global的confinement
        curr_max_val = min(a[n - 1][m - 1], a[0][0])

        # 在 0 -> max_val的区间内，作bfs,
        while curr_max_val >= 0:
            if self.exist_path(a, curr_max_val):
                return curr_max_val;
            else:
                curr_max_val -= 1

        return curr_max_val

    # 查看是否能找到一个val <= curr_max_val
    def exist_path(self, a, curr_max_val):
        n, m = len(a), len(a[0])

        visited = set([(0, 0)])
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            if x == len(a) - 1 and y == len(a[0]) - 1:
                return True;

            for dx, dy in DIRECTIONS:
                if self.is_valid(x + dx, y + dy, a, visited) and a[x + dx][y + dy] >= curr_max_val:
                    visited.add((x + dx, y + dy))
                    q.append((x + dx, y + dy))

        return False;

    def is_valid(self, x, y, a, visited):
        if x < 0 or x > len(a) - 1: return False;
        if y < 0 or y > len(a[0]) - 1: return False;
        if (x, y) in visited: return False;
        return True;



input = [[5,4,5],[1,2,6],[7,4,6]]

output = Solution().maximum_minimum_path(input)

print(output)
