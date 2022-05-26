import heapq

N = 9
heap = []
hash = {1}
heapq.heappush(heap, 1)

curr = 1

for _ in range(N):
    curr = heapq.heappop(heap)
    for multipler in [2, 3, 5]:
        val = curr * multipler
        if val not in hash:
            hash.add(val)
            heapq.heappush(heap, val);
return curr