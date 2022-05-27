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
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        points = []

        for interval in airplanes:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        max_num_planes = 0
        planes = 0

        for _, delta in sorted(points):
            planes += delta
            max_num_planes = max(planes, max_num_planes)

        return max_num_planes