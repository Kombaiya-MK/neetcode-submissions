class Solution:
    def climbStairs(self, n: int) -> int:
        dMap = {}

        for i in range(1, n + 1):
            if i in dMap:
                dMap[i] = dMap[i] + dMap[i-1]
            else:
                dMap[i] = i
        return dMap[n]
        