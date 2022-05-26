class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        dp=nums[:]
        ans = -float("inf")

        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1] + nums[i])
        return max(dp)