class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        n = len(nums)
        if n <= 1:
            return n
    
        
        currentLongestSequence = 0
        longestSequence = 0

        for currentNum in nums:
            if currentNum - 1 not in hashSet:
                currentLongestSequence = 1
                while  currentNum + 1 in hashSet:
                    currentNum += 1
                    currentLongestSequence += 1

                longestSequence = max(longestSequence, currentLongestSequence)
                


        return longestSequence

            

        