from typing import (
    List,
)
from lintcode import (
    lintcode,
)


class Solution:

    def number_of_processes(self, logs: List[Interval], queries: List[int]) -> List[int]:
        events = []

        for interval in logs:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        for q in queries:
            events.append((q, 0))

        print(sorted(events))

        running, counts = 0, {}
        for t, delta in sorted(events):
            running += delta
            if delta == 0:
                counts[t] = running

        return [counts[q] for q in queries]