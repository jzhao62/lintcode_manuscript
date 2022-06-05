from typing import (
    List,
)
from lintcode import (
    lintcode,
)




class Solution:


    def number_of_processes(self, logs: List[Interval], queries: List[int]) -> List[int]:
        events = sorted([(log.start, 1) for log in logs] +
                        [(log.end, -1) for log in logs] +
                        [(q, 0) for q in queries],
                        key=lambda e: (e[0], -abs(e[1]), e[1]))

        running, counts = 0, {}
        for t, delta in events:
            running += delta
            if delta == 0:
                counts[t] = running

        return [counts[q] for q in queries]
