from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: Sorted interval list.
    @param new_interval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals: List[Interval], new_interval: Interval) -> List[Interval]:
        left = []
        right = []
        start, end = new_interval.start, new_interval.end

        for interval in intervals:
            if interval.end < new_interval.start:
                left.append(interval)
            elif interval.start > new_interval.end:
                right.append(interval)
            else:
                start = min(start, interval.start)
                end = max(end, interval.end)

        return left + [Interval(start, end)] + right