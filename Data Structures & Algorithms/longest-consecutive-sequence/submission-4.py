class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        if n <= 1:
            return n
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
        
        currentLongestSequence = 0
        longestSequence = 0

        i = 0
        minVal = min(nums)

        for i in range(n):
            while True:
                if minVal in hashMap:
                    currentLongestSequence += 1
                    minVal = minVal + 1
                else:
                    longestSequence = max(longestSequence, currentLongestSequence)
                    currentLongestSequence = 0
                    break

        
        return longestSequence

            

        