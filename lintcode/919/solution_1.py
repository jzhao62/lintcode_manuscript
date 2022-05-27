from lintcode.intervals import Interval


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        meeting_rooms = 0
        ongoing_meetings = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            meeting_rooms = max(meeting_rooms, ongoing_meetings)

        return meeting_rooms


intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

output = Solution().minMeetingRooms(intervals)

print(output)
