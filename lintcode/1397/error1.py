from typing import (
    List,
)
from lintcode import (
    Interval,
)


class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """

    def digital_coverage(self, intervals: List[Interval]) -> int:

        output = []

        for interval in intervals:
            output.append((interval.start, 1))
            output.append((interval.end, -1))

        highest_coverage = 0
        curr_cover = 0
        for _, delta in sorted(output):
            curr_cover += delta
            highest_coverage = max(curr_cover, highest_coverage)

        return highest_coverage


input = [Interval(1, 3), Interval(2, 3), Interval(3, 4)]

