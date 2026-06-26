class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
        
        currentLongestSequence = 1
        longestSequence = 0

        i = 0

        for i in range(n):
            while True:
                if nums[i] + 1 in hashMap:
                    currentLongestSequence += 1
                    i = hashMap[nums[i] + 1]
                else:
                    longestSequence = max(longestSequence, currentLongestSequence)
                    currentLongestSequence = 0
                    break

        
        return longestSequence

            

        