import math


class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = math.inf

            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
                    # why use a break here
                    break;

        return dp[n - 1]
