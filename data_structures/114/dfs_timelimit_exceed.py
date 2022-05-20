DIRECTION = [(1, 0), (0, 1)]


class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        curr_path = []

        return self.dfs(m, n, 0, 0, curr_path)

    def dfs(self, m, n, x, y, curr_path):
        curr_path.append((x, y))

        curr_sum = 0;

        if x == m - 1 and y == n - 1:
            print(curr_path)
            return 1

        for d_x, d_y in DIRECTION:
            if self.isValid(m, n, x + d_x, y + d_y, curr_path):
                curr_sum += self.dfs(m, n, x + d_x, y + d_y, curr_path)
                curr_path.pop()
        return curr_sum

    def isValid(self, m, n, x, y, curr_path):
        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x, y) in curr_path:
            return False

        return True


ret = Solution().uniquePaths(2, 62)

print(ret)
