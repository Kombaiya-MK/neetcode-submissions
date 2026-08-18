class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for idx in range(1, len(intervals)):

            if result[-1][-1] >= intervals[idx][0]:
                result[-1][-1] = max(result[-1][-1], intervals[idx][-1])
            
            else:
                result.append(intervals[idx])
        # print(result)
        return result