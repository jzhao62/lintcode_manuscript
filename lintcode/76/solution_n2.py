class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):

        if not nums: return 0

        dp = [1] * len(nums)

        for i, m in enumerate(nums):
            for j, n in enumerate(nums[:i]):
                if (m > n): dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, A):

        if not A: return 0

        dp = [1 for _ in range(len(A))]
        for i in range(0, len(dp)):
            path = 0
            for j in range(0, i):
                if A[i] > A[j]:
                    path = max(path, dp[j])
            dp[i] = path + 1

        return max(dp)