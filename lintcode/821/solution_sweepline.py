from lintcode.lintcode import Interval


class Solution:
    """
    @param seq_a: the list of intervals
    @param seq_b: the list of intervals
    @return: the time periods
    """

    def time_intersection(self, seq_a , seq_b ):

        points = []

        for interval in seq_a + seq_b:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        interval = []
        active_user = 0
        last_timestamp = None

        for timestamp, delta in sorted(points):
            if active_user == 2:
                self.merge(interval, last_timestamp, timestamp)

            active_user += delta
            last_timestamp = timestamp

        return interval

    def merge(self, interval, start, end):
        if start is None:
            return

        if interval and interval[-1].end == start:
            interval[-1].end = end
            return;

        interval.append((Interval(start, end)))



seqA, seqB = [Interval(1,2),Interval(5,100)], [Interval(1,6)]

output = Solution().time_intersection(seqA, seqB)

print(output)