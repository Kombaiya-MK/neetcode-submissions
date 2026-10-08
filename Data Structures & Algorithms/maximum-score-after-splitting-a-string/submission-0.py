class Solution:
    def maxScore(self, s: str) -> int:
        maxOnes = 0
        maxZeros = 0
        idx = 0
        while s[idx] == '0':
            maxZeros += 1
            idx += 1
        for i in range(idx, len(s)):
            if s[i] == '1':
                maxOnes += 1
        if maxZeros == 0:
            return maxOnes - 1
        return maxOnes + maxZeros
        

        
        