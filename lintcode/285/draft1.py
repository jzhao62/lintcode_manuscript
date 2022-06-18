from typing import (
    List,
)


class Solution:

    def tall_building(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [1] * n
        self.count_building(range(n), res, arr)
        self.count_building(range(n - 1, -1, -1), res, arr)

        return res

    def count_building(self, idx_list, res, arr):
        stk = []

        for i in idx_list:
            res[i] += len(stk)
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()

            stk.append(i)


arr = [5, 3, 8, 3, 2, 5]

output = Solution().tall_building(arr)

print(output)
