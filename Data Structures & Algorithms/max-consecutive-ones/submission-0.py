class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currentOnes = 0

        for num in nums:
            if num != 0:
                currentOnes += 1
            else:
                currentOnes = 0
            maxOnes = max(maxOnes, currentOnes)
        return maxOnes
        