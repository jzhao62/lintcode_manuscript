from bisect import insort


class MyCalendarTwo:

    def __init__(self) -> None:
        self.checkpoints = []
        self.record = {}

    def book(self, start, end):
        """
        @param start: start tme
        @param end: end time
        """
        for checkpoint in [start, end]:
            if checkpoint not in self.checkpoints:
                insort(self.checkpoints, checkpoint)
                self.record[checkpoint] = 0
        self.record[start] += 1
        self.record[end] -= 1

        cnt = 0
        for checkpoint in self.checkpoints:
            cnt += self.record[checkpoint]
            if cnt >= 3:
                self.record[start] -= 1
                self.record[end] += 1
                return False
        return True




MyCalendar = MyCalendarTwo();
MyCalendar.book(10, 20);
MyCalendar.book(50, 60);
MyCalendar.book(10, 40);
MyCalendar.book(5, 15);
MyCalendar.book(5, 10);
MyCalendar.book(25, 55);