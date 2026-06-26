class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashMap = {}
        n = len(nums)
        if n <= 1:
            return n
        minNum = min(nums)
        maxNum = max(nums)
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        i, j = minNum, maxNum
        k = 0
        while i <= j:
            if i in hashMap:
                k += 1
            else:
                return k
            i += 1
        return k
            

        