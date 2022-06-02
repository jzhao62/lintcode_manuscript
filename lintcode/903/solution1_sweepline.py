from typing import (
    List,
)


class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """

    def get_modified_array(self, length, updates):
        changes = [0] * (length + 1)
        for update in updates:
            changes[update[0]] += update[2]
            changes[update[1] + 1] -= update[2]

        prefix_sum = [0] * (len(changes) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + changes[i - 1]
        return prefix_sum[1:-1]






updates = [
[1,  3,  2],
[2,  4,  3],
[0,  2, -2]
]

length = 5

output = Solution().get_modified_array(length, updates)
