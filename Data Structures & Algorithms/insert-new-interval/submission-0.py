class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        newStart, newEnd = newInterval
        for start, end in intervals:

            if end < newStart:
                result.append([start, end])

            elif start <= newEnd:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)

            else:
                result.append([newStart, newEnd])
                newStart = start
                newEnd = end

        result.append([newStart, newEnd])
        return result
            