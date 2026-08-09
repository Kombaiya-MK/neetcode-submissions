"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort()
        if not intervals:
            return True
        intervals.sort(key=lambda interval: interval.start)
        endTime = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < endTime:
                return False
            endTime = interval.end
        return True
