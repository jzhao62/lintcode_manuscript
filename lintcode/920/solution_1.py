from typing import (
    List,
)
from lintcode import (
    lintcode,
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
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:

        points = []

        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        max_meeting_rooms = 0
        onging_meetings = 0

        for _, delta in sorted(points):
            onging_meetings += delta
            max_meeting_rooms = max(max_meeting_rooms, onging_meetings)

        return not points or max_meeting_rooms == 1