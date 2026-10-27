class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost) 
        dp = [0] * (n)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for idx in range(2, n):
            dp[idx] = min(dp[idx-1], dp[idx-2]) + cost[idx]
        return min(dp[n-1], dp[n-2])




        