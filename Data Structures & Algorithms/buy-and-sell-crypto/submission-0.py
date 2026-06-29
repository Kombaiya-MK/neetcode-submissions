class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningProfit = 0
        maxAttainbaleProfit = 0
        minIdx = 0

        for idx in range(len(prices)):
            if prices[idx] < prices[minIdx]:
                minIdx = idx
            runningProfit = prices[idx] - prices[minIdx]
            maxAttainbaleProfit = max(maxAttainbaleProfit,runningProfit)
        return maxAttainbaleProfit

            

        