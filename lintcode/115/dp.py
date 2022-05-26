class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):

        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)

        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue;
                if obstacleGrid[i][j] == 1:
                    continue;

                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                    continue;
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                    continue;
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];

        for row in dp:
            print(row)

        return dp[m - 1][n - 1]
