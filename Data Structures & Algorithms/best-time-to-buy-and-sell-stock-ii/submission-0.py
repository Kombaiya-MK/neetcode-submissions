class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                maxPrice += (prices[idx] - prices[idx - 1])
        return maxPrice        

        