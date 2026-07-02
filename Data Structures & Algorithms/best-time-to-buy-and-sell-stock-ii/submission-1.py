class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            profit += max(0, prices[idx] - prices[idx-1])
        return profit        

        