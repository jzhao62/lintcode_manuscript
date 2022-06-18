from typing import (
    List,
)


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trap_rain_water(self, heights: List[int]) -> int:
        stack = []

        i, res, n = 0, 0, len(heights)

        while i < n:
            if not stack or heights[i] <= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                if not stack: continue;
                res += (min(heights[i], heights[stack[-1]] - heights[t])) * (i - stack[-1] - 1)

        return res



heights = [100,50,99,50,100,50,99,50,100,50]


x = Solution().trap_rain_water(heights)

print(x)