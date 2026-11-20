class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq = {}

        for row in wall:
            curSum = 0

            for i in range(len(row) - 1):
                curSum += row[i]

                freq[curSum] = freq.get(curSum, 0) + 1

        if not freq:
            return len(wall)

        return len(wall) - max(freq.values())