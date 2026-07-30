class Solution:
    def climbStairs(self, n: int) -> int:
        dMap = {}
        for i in range(n + 1):
            if i in dMap:
                dMap[i] = dMap[i - 2] + dMap[i-1]
            else:
                dMap[i] = i
            print(dMap)

        return dMap[n]
        