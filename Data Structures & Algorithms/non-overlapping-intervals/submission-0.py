class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        currentEnd = intervals[0][1]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < currentEnd:
                removals += 1
            else:
                currentEnd = intervals[idx][1]
        return removals