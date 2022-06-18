from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of n integers
    @return: true if there is a 132 pattern or false
    """
    def find132pattern(self, nums: List[int]) -> bool:
        # write your code here
        if len(nums) < 3:
            return False
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            while stack and nums[i] <= stack[-1]:
                stack.pop()
            stack.append(nums[i])
        if len(stack) > 1 and len(stack) < len(nums):
            return True
        return False




nums = [3, 1, 4, 2]


x = Solution().find132pattern(nums)
print(x)