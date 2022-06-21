class Solution:
    def merge(self, intervals):
        arr = []
        for a, b in intervals:
            arr.append((a, 1))
            arr.append((b, -1))

        output = []
        curr = None
        for p, delta in sorted(arr):
            self.merge_interval(output, curr, p)
            curr = p

        return output


    def merge_interval(self, output, start, end):
        if start is None:
            return;

        if output and output[-1].end == start:
            output[-1].end = end
            output.append([start, end])

intervals = [[1,3],[2,6],[8,10],[15,18]]


x = Solution().merge(intervals)
print(x)