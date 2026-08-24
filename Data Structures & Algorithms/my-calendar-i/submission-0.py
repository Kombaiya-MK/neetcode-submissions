class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:

        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        current = 0

        for time, change in self.events:
            current += change

            if current > 1:
                # Undo the booking
                self.events.remove((startTime, 1))
                self.events.remove((endTime, -1))
                return False

        return True