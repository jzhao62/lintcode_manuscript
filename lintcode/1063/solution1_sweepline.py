from bisect import insort


class MyCalendarThree:

    def __init__(self):
        self.checkpoints = []
        self.record = {}

    def book(self, start, end):
        for time in [start, end]:
            if time not in self.checkpoints:
                insort(self.checkpoints, time)
                self.record[time] = 0

        self.record[start] += 1
        self.record[end] -= 1

        cnt = 0
        output = 0

        for time in self.checkpoints:
            cnt += self.record[time]
            output = max(output, cnt)

        return output