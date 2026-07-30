class Solution:
    def climbStairs(self, n: int) -> int:
        dMap = {0:1, 1:1}
        for i in range(2, n + 1):
            dMap[i] = dMap[i - 2] + dMap[i-1]
        return dMap[n]
        