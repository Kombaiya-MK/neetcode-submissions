class Solution:
    def tribonacci(self, n: int) -> int:
        dMap = {0:0, 1:1, 2:1}
        for i in range(3, n+1):
            dMap[i] = dMap[i-1] + dMap[i-2] + dMap[i-3]
        return dMap[n]

        