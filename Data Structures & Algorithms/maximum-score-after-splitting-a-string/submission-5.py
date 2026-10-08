class Solution:
    def maxScore(self, s: str) -> int:
        totalSum = 0
        maxSum = 0
        for ch in s:
            totalSum += int(ch)
        
        zeros = 0
        curSum = 0
        ones = 0
        for ch in s:
            if ch == '0':
                zeros += 1
            else:
                ones += 1
            maxSum = max(maxSum, totalSum + zeros - ones)
        
        if ones == 0:
            return maxSum - 1
        return maxSum


        


        