from bisect import insort


class MyCalendarTwo:

    def __init__(self) -> None:
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

        for time in self.checkpoints:
            cnt += self.record[time]
            if cnt >= 3:
                self.record[start] -= 1
                self.record[end] += 1
                return False;

        return True;


MyCalendar = MyCalendarTwo();
MyCalendar.book(10, 20);
MyCalendar.book(50, 60);
MyCalendar.book(10, 40);
MyCalendar.book(5, 15);
MyCalendar.book(5, 10);
MyCalendar.book(25, 55);
